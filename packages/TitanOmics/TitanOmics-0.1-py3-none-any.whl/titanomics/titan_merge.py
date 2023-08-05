# -*- coding: utf-8 -*-
"""titan_merge.py: Module to merge paired end Illumina sequences
Uses flash2 [https://github.com/dstreett/FLASH2]

$ """

import os
import subprocess


## mergeReads
#
def mergeReads(reads, config:dict, path:os.PathLike):
    os.makedirs(path, exist_ok=True)
    
    if type(reads) is str:
        return reads

    R1 = reads[0]
    R2 = reads[1]

    try:
        # FLASH
        command = f"{config['EXE_FLASH2']} -D -O -d {path} {R1} {R2}"
        with open(f"{path}/stdout.txt", 'w') as fout, open(f"{path}/stderr.txt", 'w') as ferr:
            subprocess.run(command, shell=True, check=True, stdout=fout, stderr=ferr)
    except:
        print("Error: Failed to merge: " + command)
        return None

    return os.path.join(path, 'out.extendedFrags.fastq')
