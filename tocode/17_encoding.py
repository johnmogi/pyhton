# setting> plugins > hex- install hex editor
# delta xedit
# filehandle = open('1_arithmetic.md', 'r', encoding='UTF-8')

# open returns a file handle...
with open('1_arithmetic.md', 'r', encoding='UTF-8') as filehandle:
    first_line = filehandle.readline()
    print(first_line)
    # for line in filehandle:
    #     print(line, end='')

# filehandle.close()
# system resources are limited... therefore closing is recommended