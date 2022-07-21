import os
import subprocess

for dir in os.listdir():
    if os.path.isdir(dir) and not dir == ".git" and not dir == "MetaPhlAn2":
        os.chdir(dir)
        print(dir)
        subprocess.call(
            ["metaphlan",
            "QC_1P.fastq.gz,QC_2P.fastq.gz",
            #"--bowtie2db", database_dir,
            "--bowtie2out", "bowtieout.bowtie2.bz2",
            "--index", "mpa_v30_CHOCOPhlAn_201901",
            "--nproc", "16", "--input_type", "fastq",
            "-o", "metaphlan3.txt", "--add_viruses", "--unknown_estimation"
            ]
        )
        os.chdir("../")
