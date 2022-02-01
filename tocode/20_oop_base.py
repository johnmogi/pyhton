class Invoice:
    # def __init__(self, vat):
    #     self.vat = vat
    vat = 0.17
    def _with_vat(self, price):
        return price * (1 + self.vat)

    def print_item(self, name, price):
        print(f' {name} : {self._with_vat(price)}')


# i = Invoice(0.17)
i = Invoice()

i.print_item('iphone', 4000)
i.print_item('samsung', 3000)