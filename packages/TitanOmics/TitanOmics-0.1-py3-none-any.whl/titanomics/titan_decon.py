# -*- coding: utf-8 -*-
"""titan_decon.py: Module to clean trimmed .fastq files

UPDATE:
format the bowtie2 databases,
samtools, clean reads
"""

import os
import subprocess
import pkg_resources as pkg

REFSEQ = dict(
    Illumina = pkg.resource_filename("titanomics", "data/phix174_ill.ref.fna"),
    Lambda = pkg.resource_filename("titanomics", "data/lambda-phage.fna"),
    Pacbio = pkg.resource_filename("titanomics", "data/PacBio_quality-control.fna")
    )


# deconReads
def deconReads(rawRead, config:dict, path:os.PathLike):
    os.makedirs(path, exist_ok=True)
    key = rawRead[0]
    reads = rawRead[1]

    if 'REFSEQ' in config:
        refseq = config['REFSEQ']
    else:
        refseq = REFSEQ['Illumina']

    if type(reads) is str:
        outfile = os.path.join(path, f"unmapped_{os.path.basename(reads)}")
        inargs = f"-q {reads}"
    else:
        outR1 = f"unmapped_{os.path.basename(reads[0])}"
        outR2 = f"unmapped_{os.path.basename(reads[1])}"
        outfile = [os.path.join(path, outR1), os.path.join(path, outR2)]
        inargs = f"-1 {reads[0]} -2 {reads[1]}"

    # Bowtie2-build
    try:
        command = f"{config['EXE_BOWTIE2_BUILD']} {refseq} {path}/dbBowtie"
        with open(f"{path}/stdoutDB.txt", 'w') as fout, open (f"{path}/stderrDB.txt", 'w') as ferr:
            subprocess.run(command, shell=True, check=True, stdout=fout, stderr=ferr)
    except Exception as e:
        print(f"Error: Failed to build Bowtie2 Database:\n{e}")
        return None

    # Bowtie2
    try:
        command = f"{config['EXE_BOWTIE2']} -p {config['CPUS']} -x {path}/dbBowtie {inargs} -S {path}/local.sam --very-sensitive-local"
        with open(f"{path}/stdout.txt", 'w') as fout, open (f"{path}/stderr.txt", 'w') as ferr:
            subprocess.run(command, shell=True, check=True, stdout=fout, stderr=ferr)
    except Exception as e:
        print("Error: Failed to Map Reads:\n", e)
        return None


    #command = f"graphmap2 align -r ref.fa -d {reads} -o out.sam"

    # Samtools
    try:
        if type(reads) is str:
            command = f"{config['EXE_SAMTOOLS']} fastq -f {0x0004} {path}/local.sam >{outfile}"
            subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            command = f"{config['EXE_SAMTOOLS']} fastq -f {0x0044} {path}/local.sam >{outfile[0]}"
            subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            command = f"{config['EXE_SAMTOOLS']} fastq -f {0x0084} {path}/local.sam >{outfile[1]}"
            subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Error: Failed to extract mapped reads:\n{e}")
        return None

    
    return outfile
