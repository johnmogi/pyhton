from collections import defaultdict
import glob

counter = defaultdict(int)

py_files = glob.glob('*.py')

for file in py_files:
    counter[file] += 1

print(counter)

