class MyCounter:
    acc =0

    def __init__(self, acc):
        self.count = acc
        # print(self.count)

    def add(self):
        result = self.acc + 1
        return self.acc

    count = add(acc)




for _ in range(10):
     c1 = MyCounter(_)



# should print 10
print(MyCounter.count)