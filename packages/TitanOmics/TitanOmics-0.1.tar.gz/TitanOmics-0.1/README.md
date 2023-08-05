# TITAN

Titan is a comprehensive multi-omics data analysis pipeline. TITAN contains a modular analysis pipeline for assembly, annotation, quantification and genome binning of metagenomics. TITAN transforms raw sequence data into functional and taxonomic data at the microbial population level and provides genome-centric resolution through genome binning. TITAN is user-friendly, easy install through Bioconda maintained as open-source on GitHub.

![GitHub Logo](titan.jpg)

## Initial development phase

Titan is currently in the early phases of development, check back soon for updates.

## Installing Titan

### Option 1) Anaconda

- Anaconda install from bioconda with all dependencies:

```bash
conda create -n titan -c conda-forge -c bioconda titan -y
```

### Option 2) pip

```bash
pip install titan_omics
```

- *Dependencies should be installed manually and specified in the config file or path

### Option 3) Manual Install

*Latest code might be unstable

1. Clone github Repo

    ```bash
    git clone https://github.com/raw-lab/titan.git
    ```

2. Run Setup File

    ```bash
    cd titan
    python3 install_titan.py
    conda activate titan
    ```

- This creates an anaconda environment called "titan" with all dependencies installed.

## Input formats

- From any NextGen sequencing technology (from Illumina, PacBio, Oxford Nanopore)
- type 1 raw reads (.fastq format)
- type 2 nucleotide fasta (.fasta, .fa, .fna, .ffn format), assembled raw reads into contigs
- type 3 protein fasta (.faa format), assembled contigs which genes are converted to amino acid sequence

## Citing Titan

## CONTACT

The informatics point-of-contact for this project is [Dr. Richard Allen White III](https://github.com/raw-lab).  
If you have any questions or feedback, please feel free to get in touch by email.  
Dr. Richard Allen White III - rwhit101@uncc.edu or raw937@gmail.com.  
Jose Figueroa - jlfiguer@uncc.edu  
Or [open an issue](https://github.com/raw-lab/titan/issues).  
