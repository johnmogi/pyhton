'''
ask user 20 times for grade
calculate avg.
print all grades above avg.
'''

import sys
grades = []
num = 3
result = 0
for _ in range(num):
    grade = int(input(f'give me a grade {_}/{num}: '))
    grades.append(grade)

for g in range(num):
    print(grades[g])
    result += grades[g]

avg = result / num
good_grades = []

for grade in grades:
    if grade > avg:
        good_grades.append(grade)

print(f'your good grades are: {good_grades}')

# for arg in sys.argv:
#     print(arg)
