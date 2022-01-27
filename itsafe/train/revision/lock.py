import threading


def counter(l):
    for i in range(10000):
        with l:
            print (i)

            
lock = threading.Lock()
for i in range(100):
    threading.Thread(target=counter,args=(lock,)).start()
