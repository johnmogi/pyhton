class Light:
    on = False


a = Light()
b = Light()

Light.on = True
print(b.on)

