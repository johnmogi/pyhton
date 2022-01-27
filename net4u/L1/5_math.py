'''
operators +, -, *, /,
5 / 2 == 2.5 (float)
** 3**3 == 27
// 5//2 == 2 (int number of whole apperences - oposite to %)
'''

#num = 4567
num = int(input('enter 4 digits: '))
# thousands = num[0]
# hundreds = num[1]
# tens = num[2]
# singles = num[3]
#
# print('thousands: '+ thousands,
#       '\nhundreds: ' + hundreds ,
#       '\ntens: ' + tens,
#       '\nsingels: ' + singles  )

print('thousands: ' + str(num//1000) , '\n')
print('hundreds: ' + str((num%1000)//100) , '\n')
print('tens: ' + str((num%100)//10) , '\n')
print('singles: ' + str((num%10)//1) , '\n')

'''
thousands =[0]
hundreds = [1]
tens = [2]
singles = [3]
'''




