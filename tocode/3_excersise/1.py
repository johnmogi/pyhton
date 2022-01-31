'''
this excercise opens the password log file
checks for match in input and grants permission if correct...
'''

welcome = 'Welcome Master'
alert = 'INTRUDER ALERT'

username = input('\nenter your username: ')
password = input('enter your password: ')


def auth(u, p):
    with open('password.log', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            temp = line.split()
            user_name = temp[3]
            pass_word = temp[1].split(',')
            pass_word = pass_word[1]
            if u == user_name:
                print(f'hi, {u}')
            else:
                print(f'oops, {alert}')
                break

            if p == pass_word:
                print(f'{welcome}')
                break
            else:
                print(f'oops, something is wrong... {alert}')
                break


auth(username, password)
