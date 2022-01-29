
numbers = []

for _ in range(10):
    num = int(input('give me a number: '))
    numbers.append(num)

numbers.sort()

print(numbers[-1])
