import sys

hosts_list = sys.argv

# for list in hosts_list:
#     print(list)

with open('hosts', 'r', encoding="UTF-8") as f:
    for line in f.readlines():
        hosts = line.split("=")
        for arg in hosts_list:
            if arg == hosts[0]:
                print(f'the desired ip: {hosts[1]}')
        