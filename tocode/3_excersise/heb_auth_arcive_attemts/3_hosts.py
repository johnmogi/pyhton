'''
ask user for hostnames and ip addresses:
hostname=ipadress
# work=10.0.0.2
# router=10.0.0.1
ask user for hostnames - for each print the ip
if a hostname does not appear on the user list print appropriate error
'''
hosts_store = []

with open('../hosts', 'r', encoding="UTF-8") as f:
    while True:
        hostname = input('\ngive me a hostname, press [x] to abort: ')
        if hostname == 'x':
            break
        else:
            for line in f.readlines():
                hosts = line.split("=")
                for _ in range(len(f.readlines())):
                    hosts_store.append(hosts[0],hosts[1])
                # print(hosts)
                if hostname == hosts[0]:
                    print(f'the requested ip is: {hosts[1]}')
                    break
                else:
                    break

print(hosts_store)


