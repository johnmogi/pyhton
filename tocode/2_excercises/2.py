'''
this functions tries to convert the user/'s age into months
an error exception will be raised if user input is not legal.
'''

def age_to_months(age):
    result = age * 12
    return result

try:
    age = int(input('what\'s your age? '))
    print(f'your age in months: { age_to_months(age)}')
except:
    print('sorry, you can only input numbers...')
