import os
for dir in os.listdir():
    if not os.path.isdir(dir) or dir == ".git" or dir == "MetaPhlAn2":
        continue
    os.rename(dir + f"/{dir}.txt", dir + f"/{dir}_metaphlan2.txt")
