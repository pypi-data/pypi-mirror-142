# -*- coding: utf-8 -*-
"""titan_assembly.py: Module to assembe .fastq files

-runs megahit assembler from merged PE Illumina IL+Ext or SE Pacbio or Nanopore
-add flag to run Megahit OR Spades
-include step for flye for PacBIO and Nanopore
* make options available in config file and in master


$ megahit -1 pe_1.fq -2 pe_2.fq -o out  # 1 paired-end library
$ megahit --12 interleaved.fq -o out # one paired & interleaved paired-end library
$ megahit -1 a1.fq,b1.fq,c1.fq -2 a2.fq,b2.fq,c2.fq -r se1.fq,se2.fq -o out # 3 paired-end libraries + 2 SE libraries
"""

import os
import shutil
import subprocess


## assembleSingleEndReads
#
def assembleReads(fastq, config, path):
    os.makedirs(os.path.join(path, 'assembly'), exist_ok=True)
    shutil.rmtree(os.path.join(path, 'assembly'), ignore_errors=True)
    
    if type(fastq) is str:
        infile = f"-r {fastq}"
    else:
        infile = f"-1 {fastq[0]} -2 {fastq[1]}"
    outfile = os.path.join(path, 'assembly', 'final.contigs.fa')

    command = f"{config['EXE_MEGAHIT']} {infile} -o {os.path.join(path, 'assembly')}"
    
    try:
        with open(f"{path}/stdout.txt", 'w') as fout, open(f"{path}/stdout.txt", 'w') as ferr:
            subprocess.run(command, shell=True, check=True, stdout=fout, stderr=ferr)
    except:
        print("Failed to execute", command)

    return outfile
