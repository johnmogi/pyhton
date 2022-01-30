import fileinput

# for line in fileinput.input():
#     print(f':> {line}')
# ^d to stop

for line in fileinput.input('1_arithmetic.md'):
    print(f'{line}')