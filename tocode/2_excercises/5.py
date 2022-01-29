import random

num1 = random.randint(1,10)
num2 = random.randint(1,10)

def find_lowest_denom(num1,num2):
    i = 2
    while True:
        print(f'attempting to locate the lowest dividable number: {i}')
        if i % num1 == 0 and i % num2 == 0 :
            print(f'match: {num1, i}')
            print(f'match: {num2, i}')
            break
        i = i + 1

find_lowest_denom(num1,num2)