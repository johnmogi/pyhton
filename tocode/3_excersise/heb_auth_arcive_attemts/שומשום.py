welcome = 'שומשום נפתח עבורך אדוני'
alert = 'השודדים באים, נוס על חייך פולש!'
tries = 0
with open('סיסמאות.txt', 'r', encoding='UTF-8') as f:
    file_content = f.readlines()
    print(file_content, end="")
    username = input(f"מי מעז להטריד את שלוותי? \n")
    # this happens now 4 times, hence the loop:
    for line in file_content:
        tries = tries + 1
        if tries > 3:
            print(alert)
            break
        temp = line.split()
        user_name = temp[3]
        # print(f'user_name: {user_name}')
        if username == user_name:
            print(f'שלום ,{username} ')
            pass_word = temp[1].split(',')
            pass_word = pass_word[0]
            # print(f'pass_word: {pass_word}')
            password = input('מה הסיסמה הסודית ביותר ביקום כולו: ')
            if password == pass_word:
                print(welcome)
                break
            else:
                print(alert)

