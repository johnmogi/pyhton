sentences = []

while True:
    user_say = input('say something or nothing at all: ')
    sentences.append(user_say)
    if user_say == '':
        if len(sentences) != 0:
            for s in sentences:
                print(f'user said {s[::-1]}')
    else:
        continue

    break




