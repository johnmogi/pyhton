import multiprocessing


def counter(number):
    for i in range(number):
        print(i)

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=counter, args=(100000,))
        p.start()