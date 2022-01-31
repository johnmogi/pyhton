# w - creates and writes into the file
# a - creates and adds into the file

with open('new-file.txt', 'w', encoding='UTF=8') as f:
    f.write('My name is file montigio\n')
    f.write('you created this file with python... \n')
    f.write(('prepare to die!!!\n'))

