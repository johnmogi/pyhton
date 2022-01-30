import glob
import os.path

all_files = glob.glob('*.*')

print(all_files)

# base , ext = os.path.splitext('10_glob.py')
# print(base, ext)

# for file in all_files:
#     print(file)
counter = {}
for file_name in all_files:
    _ , ext = os.path.splitext(file_name)
    try:
        counter[ext] += 1
    except KeyError:
        counter[ext] = 1

print(counter)
# file_index = {
#     ext : os.path.splitext('.py')
#     for ext in all_files.items()
# }

# print(file_index)

# defaultdict
# Counter