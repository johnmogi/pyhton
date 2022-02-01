'''
either i should study sys.agrv or understand why this only works once:

'''
with open('../hosts', 'r', encoding="UTF-8") as f:
    while True:
        hostname = input('\ngive me a hostname, press [x] to abort: ')
        for line in f.readlines():
            hosts = line.split("=")
            if hostname == 'x':
                break
            elif hostname == hosts[0]:
                print('ip')
                continue

