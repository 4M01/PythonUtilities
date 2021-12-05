import os
from os import listdir
from os.path import isfile, join

parent_dir = "C:/Amol/Learn Kubernetes in a Month of Lunches video edition/"

with open(parent_dir + "Details.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

os.chdir(parent_dir)
onlyfiles = sorted(filter(os.path.isfile, os.listdir('.')),
                   key=os.path.getmtime)

print(onlyfiles)
counter = 0
for line in lines:
    if ("\t" not in line):
        counter = counter + 1
        line = str(counter) + " " + line
        path = os.path.join(parent_dir, line)
        os.mkdir(path)
        print("Directory '% s' created" % line)

counter = 0
for file in onlyfiles:
    counter = counter + 1
    abs_path = parent_dir + file
    base = os.path.splitext(file)[0]
    newFileName = parent_dir + str(counter) + " " + base + ".mp4"
    # newFileName = parent_dir + " " + base + ".mp4"
    os.rename(abs_path, newFileName)