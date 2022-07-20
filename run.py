import os
import subprocess

for dir in os.listdir():
    if os.path.isdir(dir) and not dir == ".git":
        os.chdir(dir)
        forward = dir + "_1.fastq"
        backward = dir + "_2.fastq"
        if forward not in os.listdir():
            os.chdir("../")
            continue
        print(os.listdir())
        command = f"gmhi --fastq1 {forward} --fastq2 {backward} -o GMHI.txt"
        subprocess.call(command.split())
        os.chdir("../")
