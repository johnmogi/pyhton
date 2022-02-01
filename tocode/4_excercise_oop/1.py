class Summer:
    result = 0

    def __init__(self):
        pass

    def add(self, num1, num2 = 0):
        if num2 > 0 :
            self.result = num1 + num2
        else:
            self.result += num1
        return self.result

    def print_total(self):
        print(self.result)


s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
s.print_total()

# should print 50
t.print_total()