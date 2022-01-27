import random

attempts = 0
guess =0

def startMenu():
    print('''
    Welcome to the guessing game...
    load last game > press [l]
    start a new game> press [s]
    exit game > press [x]
    ''')
    menu = input(': ')
    if menu == 'x':
        print('goodbye, game aborted...')
        exit(0)
    elif menu == 'l':
        pass
    elif menu == 's':
        max = int(input('set the game highest number: '))
        # todo: handle x again here...
        rand = random.randint(1,max)
        guessGame(rand, max, attempts)

def guessGame(rand, max, attempts):
    while True:
        guess = input('enter your guess from 1-{0}, [x] to exit: '.format(max))
        try:
            if guess == 'x':
                print('goodbye, game aborted...')
                exit(0)
            else:
                guess = int(guess)
        except:
                guess = int(guess)

        if guess > rand :
            attempts = attempts + 1
            print('you\'re number is too big, try again... ', rand, attempts)
        elif guess < rand :
            attempts = attempts + 1
            print('you\'re number is too small, try again... ', rand, attempts)
        else:
            print('you won! it only took you: {0} attempts... congratulations!'.format(attempts))
            exit(0)

if __name__ == '__main__' :
    startMenu()