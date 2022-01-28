'''
find out a seq number...
ask user for a num
ask user for the gap
ask the user in length
'''
numbers = []
num = int(input('give me the base number: '))
gap = int(input('give me the gap between: '))
max = int(input('give me the size of the list: '))

numbers.append(num)
jump = num + gap

for i in range(max -1):
    numbers.append(jump)
    jump = gap + jump

print(numbers)
