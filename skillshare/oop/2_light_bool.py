class Light:
    def __init__(self):
        is_light = False
        # print('light bulb created...')


    def light_on(self):
        is_light = True
        print('light on')

    def light_off(self):
        is_light = False
        print('light off')

bulb1 = Light()
bulb2 = Light()

bulb1.light_on()
bulb1.light_on()


