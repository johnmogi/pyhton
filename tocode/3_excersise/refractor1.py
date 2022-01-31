welcome = 'Welcome Master'
alert = 'INTRUDER ALERT'

with open('password.log', 'r', encoding='UTF-8') as f:
    file_content = f.readlines()
    username = input('\nenter your username: ')

    # this happens now 4 times, hence the loop:
    for line in file_content:
        temp = line.split()
        user_name = temp[3]
        # print(f'user_name: {user_name}')
        if username == user_name:
            print(f'Hello {username}')
            pass_word = temp[1].split(',')
            pass_word = pass_word[0]
            # print(f'pass_word: {pass_word}')
            password = input('enter your password: ')
            if password == pass_word:
                print(welcome)
                break
            else:
                print(alert)

