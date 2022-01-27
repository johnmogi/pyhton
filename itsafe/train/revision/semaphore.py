import threading


def counter(s):
    for i in range(10000):
        with s:
            print (i)


semaphore = threading.Semaphore(1)
for i in range(100):
    threading.Thread(target=counter,args=(semaphore,)).start()
