import random

while True:
    rand = random.randint(1, 1000000)
    print(f'trying to find a number: {rand}')
    if rand % 7 == 0 and rand % 13 == 0 and rand % 15 == 0:
        print('match found! number divides by 7, 13 and 15: {0}'.format(rand))
        break
