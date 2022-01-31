import glob
import os.path
import collections

all_files_with_extentions = glob.glob('*.*')

extentions = [
    os.path.splitext(fname)[1]
    for fname in all_files_with_extentions
]

counter = collections.Counter(extentions)

print(counter)