import threading


def counter(number):
    for i in range(number):
        print(i)

for i in range(5):
    t = threading.Thread(target=counter,args=(100000,))
    t.start()

if __name__ == '__main__':
    counter(3)