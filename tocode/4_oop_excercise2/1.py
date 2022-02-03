class Summer:
    total = 0

    # def __init__(self):
    #     return self.total 

    def add(self, num1, num2 =0):
        if num2 >0:
            self.total = num1 + num2
        else:
            self.total += num1
        return self.total
    
    def print_total(self):
        print(self.total)
    
        
    
s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
s.print_total()

# should print 50
t.print_total()