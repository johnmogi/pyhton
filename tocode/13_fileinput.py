import fileinput

# for line in fileinput.input():
#     print(f':> {line}')
# ^d to stop
unique_words = set()

for line in fileinput.input('1_arithmetic.md'):
    words = line.split()
    # unique_words.add(x) -> add one

    for w in words:
        w.lower()
        unique_words.update(words)

    # print(f'{line}', end = '')

print(unique_words)