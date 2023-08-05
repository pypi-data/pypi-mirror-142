# -*- coding: utf-8 -*-
"""titan_qc.py: Module for checking quality of .fastq files
Uses FastQC [https://www.bioinformatics.babraham.ac.uk/projects/fastqc/]
$ fastqc file.fastq
$ fastqc file_R1.fastq fastqc file_R2.fastq
"""

import os
import subprocess


## checkSingleQuality
#
def checkReads(fastq_reads, outpath:os.PathLike, exe_fastqc:str='fastqc'):
    os.makedirs(outpath, exist_ok=True)

    if type(fastq_reads) is str:
        command = f"{exe_fastqc} -o {outpath} {fastq_reads}"
        outfile = os.path.join(outpath, os.path.splitext(os.path.basename(fastq_reads))[0]+'_fastqc.html')
    else:
        command = f"{exe_fastqc} -o {outpath} {fastq_reads[0]} {fastq_reads[1]}"
        outfile = [
            os.path.join(outpath, os.path.splitext(os.path.basename(fastq_reads[0]))[0]+'_fastqc.html'),
            os.path.join(outpath, os.path.splitext(os.path.basename(fastq_reads[1]))[0]+'_fastqc.html')
        ]

    try:
        with open(f"{outpath}/stdout.txt", 'w') as fout, open(f"{outpath}/stderr.txt", 'w') as ferr:
            subprocess.run(command, shell=True, check=True, stdout=fout, stderr=ferr)
        return outfile
    except Exception as e:
        print(f"Failed to run fastqc\n{fastq_reads}\n{command}:\n{e}")

    return None
