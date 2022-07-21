import os
for dir in os.listdir():
    if not os.path.isdir(dir) or dir == ".git" or dir == "MetaPhlAn2":
        continue
    os.rename(dir + f"/metaphlan3.txt", dir + f"/{dir}_metaphlan3.txt")
