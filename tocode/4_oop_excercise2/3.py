class Widget:
    name = ''
    companion = []

    def __init__(self, name, companion = []):
        self.name = name
        self.companion = companion

    def add_dependency(self, *args):
        for arg in args:
            self.companion.append(arg.name)




luke    = Widget("Luke")
hansolo = Widget("Han Solo")
leia    = Widget("Leia")
yoda    = Widget("Yoda")
padme   = Widget("Padme Amidala")
anakin  = Widget("Anakin Skywalker")
obi     = Widget("Obi-Wan")
darth   = Widget("Darth Vader")
_all    = Widget("")


luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
# obi.add_dependency(yoda)
# darth.add_dependency(anakin)
print(luke.companion)
#
# _all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
# _all.build()
# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)


