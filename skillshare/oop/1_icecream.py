class Icecream:
    def __init__(self):
        # print('Ice cream created')
        self.scoops = 3

    def eat(self, scoops):
       # self.scoops = self.scoops - scoops
       self.scoops -= scoops
        # print('hi')

    def add(self, scoops):
        self.scoops += scoops

ice = Icecream()
sugar_cone = Icecream()

ice.add(2)
print(ice.scoops, sugar_cone.scoops)
