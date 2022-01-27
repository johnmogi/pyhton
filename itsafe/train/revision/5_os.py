import os

# fetch readme file - extract links...
#fd = open("README.md.txt","r")
# open and not os.open !

with open("README.md.txt", "r") as fd:
    lines = fd.readlines()
    for line in lines:
        print(line.find('http'))

