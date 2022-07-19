import os

for d in os.listdir():
    if d.endswith(".gz"):
        old = d
        dir = "_".join(old.split("_")[0:2])
        if not os.path.isdir(dir):
            os.mkdir(dir)
        new = dir + "/" + old
        os.rename(old, new)
