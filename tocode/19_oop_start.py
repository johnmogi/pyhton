class LightBulb:
    def __init__(self):
        self.is_light_on = False

    def light_on(self):
        if not self.is_light_on:
            print('Light on')
            self.is_light_on = True

    def light_off(self):
        if not self.is_light_on:
            print('Light off')
            self.is_light_on = True

l1 = LightBulb()
l2 = LightBulb()

l1.light_on()

print(l1.is_light_on)
print(l2.is_light_on)
