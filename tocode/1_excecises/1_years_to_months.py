'''
ask user for age, return months...
'''

# age = int(input('What\'s your age? '))
# months = age * 12
# print(f'your monthly age is: {months}')

months = int(input('What\'s your age in months? '))
age = int(months / 12)
print(f'your monthly age is: {age}')