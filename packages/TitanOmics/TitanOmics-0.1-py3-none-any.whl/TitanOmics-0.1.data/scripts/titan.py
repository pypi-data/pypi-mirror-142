#!python
# -*- coding: utf-8 -*-

"""titan-pipeline.py: 


"""


__version__ = "0.1"
__author__ = "Jose Figueroa"


import sys
import os
import configargparse as argparse #replace argparse with: https://pypi.org/project/ConfigArgParse/
import pkg_resources as pkg #to import package data files
import time
import datetime
import ray


# our package import.
from titanomics import (
    titan_qc, titan_decon, titan_merge, titan_trim, titan_assembly
)


##### Global Variables #####

# known file extensions
FILES_FASTQ = ['.fastq', '.fastq.gz']
FILES_FASTA = [".fasta", ".fa", ".fna", ".ffn", ".fasta.gz", ".fa.gz", ".fna.gz", ".ffn.gz"]
FILES_AMINO = [".faa", ".faa.gz"]


# external dependencies
DEPENDENCIES = dict(
    EXE_FASTQC = 'fastqc',
    EXE_BOWTIE2 = 'bowtie2',
    EXE_BOWTIE2_BUILD = 'bowtie2-build',
    EXE_SAMTOOLS = 'samtools',
    EXE_FLASH2 = 'flash2',
    EXE_FASTP = 'fastp',
    EXE_MEGAHIT = 'megahit'
    )

# step names
STEP = {
    1:"step_01-loadFiles",
    2:"step_02-QC",
    3:"step_03-decon",
    4:"step_04-merge",
    5:"step_05-trim",
    6:"step_06-assemble",
    7:"step_07-subsampler",
    8:"step_08-coverage",
    9:"step_09-stats",
    10:"step_10-binning",
    11:"step_11-orf_calling",
    12:"step_12-annotation",
    13:"step_13-parser",
    14:"step_14-counting",
    15:"step_15-report"
    }


## PRINT to stderr ##
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    return

def logTime(dirout, host, funcName, path, time):
    with open(f'{dirout}/time.tsv', 'a+') as outTime:
        print(host, funcName, time, path, file=outTime, sep='\t')
    return


## Ray Worker Threads
@ray.remote
def rayWorker(key, func, params:list):
    #logTime(config["DIR_OUT"], socket.gethostname(), func.__name__, path, time.strftime("%H:%M:%S", time.localtime()))
    #start = time.time()
    ret = func(*params)
    #end = str(datetime.timedelta(seconds=time.time()-start)) #time.strftime("%H:%M:%S", time.gmtime(time.time()-start))
    #logTime(config["DIR_OUT"], socket.gethostname(), func.__name__, path, end)
    return (key, ret)


## MAIN
def main():
    ## Parse the command line
    parser = argparse.ArgumentParser(add_help=False)
    parser.set_defaults()
    # At least one of these options are required
    required = parser.add_argument_group('''Required arguments
At least one sequence is required.
<accepted formats {.fastq .fasta .faa .fna .ffn .rollup}>
Example:
> titan-pipeline.py --prodigal file1.fasta
> titan-pipeline.py --config file.config
*Note: If a sequence is given in .fastq format, one of --nanopore, --illumina, or --pacbio is required.''')
    required.add_argument('-c', '--config', help = 'Path to config file, command line takes priority', is_config_file=True)
    required.add_argument('--prodigal', action='append', default=[], help='Prokaryote nucleotide sequence (includes microbes, bacteriophage)')
    required.add_argument('--fraggenescan', action='append', default=[], help='Eukaryote nucleotide sequence (includes other viruses, works all around for everything)')
    required.add_argument('--meta', action="append", default=[], help="Metagenomic nucleotide sequences (Uses prodigal)")
    required.add_argument('--super', action='append', default=[], help='Run sequence in both --prodigal and --graggenescan modes')
    required.add_argument('--protein', '--amino', action='append', default=[], help='Protein Amino Acid sequence')
    # Raw-read identification
    readtype = parser.add_mutually_exclusive_group(required=False)
    readtype.add_argument('--illumina', action="store_true", help="Specifies that the given FASTQ files are from Illumina")
    readtype.add_argument('--nanopore', action="store_true", help="Specifies that the given FASTQ files are from Nanopore")
    readtype.add_argument('--pacbio', action="store_true", help="Specifies that the given FASTQ files are from PacBio")
    # optional flags
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('--dir_out', type=str, default='./', help='path to output directory, creates "pipeline" folder. Defaults to current directory.')
    optional.add_argument('--scaffolds', action="store_true", help="Sequences are treated as scaffolds")
    optional.add_argument('--minscore', type=float, default=25, help="Filter for parsing HMMER results")
    optional.add_argument('--cpus', type=int, help="Number of CPUs to use per task. System will try to detect available CPUs if not specified")
    optional.add_argument('--chunker', type=int, default=0, help="Split files into smaller chunks, in Megabytes")
    optional.add_argument('--replace', action="store_true", help="Flag to replace existing files. False by default")
    optional.add_argument('--hmm', type=str, default='', help="Specify a custom HMM file for HMMER. Default uses downloaded FOAM HMM Database")
    optional.add_argument('--adapters', type=str, default='', help="FASTA File containing adapter sequences for trimming")
    optional.add_argument('--version', '-v', action='version',
                        version=f'Titan: \n version: {__version__} June 24th 2021',
                        help='show the version number and exit')
    optional.add_argument("-h", "--help", action="help", help="show this help message and exit")
    # Hidden from help, expected to load from config file
    dependencies = parser.add_argument_group()
    for key,value in DEPENDENCIES.items():
        dependencies.add_argument(f"--{key}", default=value, help=argparse.SUPPRESS)
    dependencies.add_argument('--control_seq', type=str, help="FASTA File containing control sequences for decontamination")

    args = parser.parse_args()

    print("\nStarting Titan Pipeline\n")

    # Merge related arguments
    if args.super:
        args.prodigal += args.super
        args.fraggenescan += args.super

    # Initialize Config Dictionary
    config = {}
    config['PATH'] = os.path.dirname(os.path.abspath(__file__))
    config['EXE_FGS+'] = os.path.join(config['PATH'], 'FGS+', 'FGS+')#pkg.resource_filename("cerberus_data", "FGS+")
    config['STEP'] = STEP
    
    # load all args into config
    for arg,value in args.__dict__.items():
        if value is not None:
            if arg == "control_seq": arg = "refseq"
            arg = arg.upper()
            if type(value) is str and os.path.isfile(value):
                value = os.path.abspath(os.path.expanduser(value))
            config[arg] = value

    # Create output directory
    config['DIR_OUT'] = os.path.abspath(os.path.expanduser(os.path.join(args.dir_out, "pipeline")))
    os.makedirs(config['DIR_OUT'], exist_ok=True)

    # Sequence File extensions
    config['EXT_FASTA'] = FILES_FASTA
    config['EXT_FASTQ'] = FILES_FASTQ
    config['EXT_AMINO'] = FILES_AMINO


    # Initialize RAY for Multithreading
    try:
        ray.init(address='auto') # First try if ray is setup for a cluster
    except:
        ray.init()
    # Get CPU Count
    if 'CPUS' not in config:
        config['CPUS'] = int(ray.available_resources()['CPU'])
    print(f"Running RAY on {len(ray.nodes())} node(s)")
    print(f"Using {config['CPUS']} CPUs per node")


    startTime = time.time()
    # Step 1 - Load Input Files
    print("\nSTEP 1: Loading sequence files:")
    fastq = {}
    fasta = {}
    amino = {}
    # Load protein input
    for item in args.protein:
        item = os.path.abspath(os.path.expanduser(item))
        if os.path.isfile(item):
            name, ext = os.path.splitext(os.path.basename(item))
            if ext in FILES_AMINO:
                amino['Protein_'+name] = item
            else:
                print(f'{item} is not a valid protein sequence')
        elif os.path.isdir(item):
            for file in os.listdir(item):
                ext = os.path.splitext(file)[1]
                if ext in FILES_AMINO:
                    args.protein.append(os.path.join(item, file))
    # Load prodigal input
    for item in args.prodigal:
        item = os.path.abspath(os.path.expanduser(item))
        if os.path.isfile(item):
            name, ext = os.path.splitext(os.path.basename(item))
            if ext in FILES_FASTQ:
                fastq['prodigal_'+name] = item
            elif ext in FILES_FASTA:
                fasta['prodigal_'+name] = item
            elif ext in FILES_AMINO:
                print(f"WARNING: Ignoring protein sequence '{item}', please use --protein option for these.")
        elif os.path.isdir(item):
            for file in os.listdir(item):
                ext = os.path.splitext(file)[1]
                if ext in FILES_FASTQ + FILES_FASTA:
                    args.prodigal.append(os.path.join(item, file))
        else:
            print(f'{item} is not a valid sequence')
    # Load FGS+ input
    for item in args.fraggenescan:
        item = os.path.abspath(os.path.expanduser(item))
        if os.path.isfile(item):
            name, ext = os.path.splitext(os.path.basename(item))
            if ext in FILES_FASTQ:
                fastq['FragGeneScan_'+name] = item
            elif ext in FILES_FASTA:
                fasta['FragGeneScan_'+name] = item
            elif ext in FILES_AMINO:
                print(f"WARNING: Ignoring protein sequence '{item}', please use --protein option for these.")
        elif os.path.isdir(item):
            for file in os.listdir(item):
                ext = os.path.splitext(file)[1]
                if ext in FILES_FASTQ + FILES_FASTA:
                    args.fraggenescan.append(os.path.join(item, file))
        else:
            print(f'{item} is not a valid sequence')
    # Load metagenomic input
    for item in args.meta:
        item = os.path.abspath(os.path.expanduser(item))
        if os.path.isfile(item):
            name, ext = os.path.splitext(os.path.basename(item))
            if ext in FILES_FASTQ:
                fastq['meta_'+name] = item
            elif ext in FILES_FASTA:
                fasta['meta_'+name] = item
            elif ext in FILES_AMINO:
                print(f"WARNING: {item} is a protein sequence, please use --prot option for these.")
                amino[name] = item
        elif os.path.isdir(item):
            for file in os.listdir(item):
                ext = os.path.splitext(file)[1]
                if ext in FILES_FASTQ + FILES_FASTA:
                    args.meta.append(os.path.join(item, file))
        else:
            print(f'{item} is not a valid sequence')
    
    print(f"Processing {len(fastq)} fastq sequences")
    print(f"Processing {len(fasta)} fasta sequences")
    print(f"Processing {len(amino)} protein Sequences")

    # Step 3 (check quality of fastq files)
    jobsQC = []
    jobsDecon = []
    if fastq:
        # Merge Paired End Reads
        fastqPaired = {k:v for k,v in fastq.items() if "R1.fastq" in v and v.replace("R1.fastq", "R2.fastq") in fastq.values() }
        for key,value in fastqPaired.items():
            reverse = fastq.pop(key.replace("R1", "R2"))
            fastq[key] = [value,reverse]
        del fastqPaired # memory cleanup
        
        print("\nSTEP 2: Checking quality of fastq files")
        for key,value in fastq.items():
            jobsQC.append(rayWorker.remote(key, titan_qc.checkReads, [value, f"{config['DIR_OUT']}/{STEP[2]}/{key}"]))
        print("\nSTEP 3: Cleaning and Assembling fastq files")
        for key,value in fastq.items():
            # Step 3 (Decon)
            jobsDecon.append(rayWorker.remote(key, titan_decon.deconReads, [(key,value), config, f"{config['DIR_OUT']}/{STEP[3]}/{key}"]))

    jobsTrim = []
    jobsMerge = []
    jobsAssemble = []
    while jobsDecon + jobsMerge + jobsTrim + jobsAssemble:
        ready,jobsDecon = ray.wait(jobsDecon, timeout=0)
        if ready:
            key,value = ray.get(ready[0])
            if value:
                fastq[key] = value
                # Step 4 (Merge)
                jobsMerge.append(rayWorker.remote(key, titan_merge.mergeReads, [value, config, f"{config['DIR_OUT']}/{STEP[4]}/{key}"]))
        
        ready,jobsMerge = ray.wait(jobsMerge, timeout=0)
        if ready:
            key,value = ray.get(ready[0])
            if value:
                fastq[key] = value
                # Step 5 (Trim)
                jobsTrim.append(rayWorker.remote(key, titan_trim.trimReads, [(key,value), config, f"{config['DIR_OUT']}/{STEP[5]}/{key}"]))
        
        ready,jobsTrim = ray.wait(jobsTrim, timeout=0)
        if ready:
            key,value = ray.get(ready[0])
            if value:
                fastq[key] = value
                # Step 5 QC
                jobsQC.append(rayWorker.remote(key, titan_qc.checkReads, [value, f"{config['DIR_OUT']}/{STEP[5]}/{key}/QC"]))
                # Step 6 Assemble
                jobsAssemble.append(rayWorker.remote(key, titan_assembly.assembleReads, [value, config, f"{config['DIR_OUT']}/{STEP[6]}/{key}"]))
        ready,jobsAssemble = ray.wait(jobsAssemble, timeout=0)
        if ready:
            key,value = ray.get(ready[0])
            if value:
                fasta[key] = value

    # Wait for misc jobs
    jobs = jobsQC
    ready, jobs = ray.wait(jobs, num_returns=len(jobs), timeout=1) # clear buffer
    while(jobs):
        print(f"Waiting for {len(jobs)} jobs:")
        ready, jobs = ray.wait(jobs)


    # Finished!
    print("\nFinished Pipeline")
    end = str(datetime.timedelta(seconds=time.time()-startTime)) #end = time.strftime("%H:%M:%S", time.gmtime(time.time()-startTime))
    #logTime(config["DIR_OUT"], socket.gethostname(), "Total_Time", config["DIR_OUT"], end)

    return 0


## Start main method
if __name__ == "__main__":
    sys.exit(main())

## End of script
