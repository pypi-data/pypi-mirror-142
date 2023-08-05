# -*- coding: utf-8 -*-
"""titan_trim.py: Module for trimming .fastq files
Uses fastp [https://github.com/OpenGene/fastp#quality-filter]

$ fastp -i in.fq.gz -o trim.fq.gz
$ fastp -i in.R1.fq.gz -I in.R2.fq.gz -o trim.R1.fq.gz -O trim.R2.fq.gz
"""

import os
import subprocess
import pkg_resources as pkg #to import package data files

ADAPTERS = pkg.resource_filename("titanomics", "data/adapters.fna")

# trimReads
def trimReads(rawRead, config:dict, path:os.PathLike):
    os.makedirs(path, exist_ok=True)
    
    key = rawRead[0]
    reads = rawRead[1]

    if 'ADAPTER' in config:
        adapters = config['ADAPTERS']
    else:
        adapters = ADAPTERS

    if type(reads) is str:
        outfile = os.path.join(path, f"trimmed_{key}.fastq")
        inargs = f"-i {reads}"
        outargs = f"-o {outfile}"
    else:
        outR1 = f"trimmed_{os.path.basename(reads[0])}"
        outR2 = f"trimmed_{os.path.basename(reads[1])}"
        outfile = [os.path.join(path, outR1), os.path.join(path, outR2)]
        inargs = f"-i {reads[0]} -I {reads[1]}"
        outargs = f"-o {outfile[0]} -O {outfile[1]}"

    command = f"{config['EXE_FASTP']} {inargs} {outargs} -p 20 -M 30 -q 30 --low_complexity_filter --adapter_fasta {adapters} -h {path}/fastp.{key}.html -j {path}/fastp.{key}.json"

    try:
        with open(f"{path}/stdout.txt", 'w') as fout, open (f"{path}/stderr.txt", 'w') as ferr:
            subprocess.run(command, shell=True, check=True, stdout=fout, stderr=ferr)
    except Exception as e:
        print("Error: Failed to Trim Reads:\n", e)
        return None

    return outfile
