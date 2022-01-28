numbers = []
for i in range(3):
    num = int(input('give me a number: '))
    numbers.append(num)

numbers.sort()
print(numbers[-1])