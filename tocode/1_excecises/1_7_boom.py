num = int(input('enter a number> '))
test = str(num).find('7')

if  num / 7 == 0:
    print('BOOM')
elif test == 0 or test == 1:
    print('BOOM')
else:
    print(test)

