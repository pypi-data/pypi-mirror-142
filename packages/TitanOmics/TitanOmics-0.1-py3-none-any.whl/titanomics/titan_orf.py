# -*- coding: utf-8 -*-
"""titan_orf.py: Module for finding Open Reading Frames from nucleotide contigs
-This will run prodigal for now (PROKKA for prokaryotes next, future FGS+)
-Instead of converter.py orfcalling.py last step converts gff to gtf
"""

import os
import subprocess


## findORF
def findORF(contig, config, subdir):
    path = f"{config['DIR_OUT']}/{subdir}"
    os.makedirs(path, exist_ok=True)
    fout = open(f"{path}/stdout.txt", 'w')
    ferr = open(f"{path}/stderr.txt", 'w')
    FGStrain = f"{os.path.dirname(config['EXE_FGSPP'])}/train"

    # Prodigal
    try:
        command = f"{config['EXE_PRODIGAL']} -i {contig} -o {path}/genes.gff -a {path}/proteins.faa -f gff"
        subprocess.run(command, shell=True, check=True, stdout=fout, stderr=ferr)
    except:
        print("Error: failed to run: " + command)

    # FragGeneScanPlusPlus
    try:
        command = f"{config['EXE_FGSPP']} -s {contig} -o {path}/output -w 0 -r {FGStrain} -t complete -p {config['CPUS']}"
        subprocess.run(command, shell=True, check=True, stdout=fout, stderr=ferr)
    except:
        print("Error: failed to run: " + command)

    # Barrnap
    try:
        command = f"{config['EXE_BARRNAP']} --quiet {contig} > {path}/barrnap.gff"
        subprocess.run(command, shell=True, check=True, stdout=fout, stderr=ferr)
    except:
        print("Error: failed to run: " + command)


    fout.close()
    ferr.close()
    return f"{path}/genes.gff"
