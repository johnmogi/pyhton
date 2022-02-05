class Light:
    is_light_on = False

    def __init__(self):
        pass
        # print('light created')

    def toggle(self):
        # if not self.is_light_on:
        #     self.is_light_on = True
        # else:
        #     self.is_light_on = False
        self.is_light_on = not self.is_light_on

bulb1 = Light()
bulb2 = Light()

bulb1.toggle()
bulb2.toggle()
bulb1.toggle()

print(bulb1.is_light_on)
print(bulb2.is_light_on)
