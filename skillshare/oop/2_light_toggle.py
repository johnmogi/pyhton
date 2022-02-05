class Light:
    def __init__(self):
        # print('toggle on and off')
        self.on = False

    def toggle(self):
        # if self.on:
        #     self.on = False
        # else:
        #     self.on = True
        self.on = not self.on

    def is_on(self):
        return self.on
        # if self.on:
        #     print('it\'s on')
        # else:
        #     print('it\'s off')



switch1 = Light()
switch2 = Light()

switch2.toggle()

print(switch1.is_on())
print(switch2.is_on())

