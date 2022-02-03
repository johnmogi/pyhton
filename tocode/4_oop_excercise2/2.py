class MyCounter:
    result = 0

    def count(self):
        return 1
        # self.result += self.result
        # return self.result

for _ in range(10):
     c1 = MyCounter()

# should print 10
print(MyCounter.count)