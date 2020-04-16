import sys
import random


def main():
    print('### Greater-Minder - The ultimate fun breaker! ###')

    begin = None
    while begin is None:
        begin = input('Let\'s play the game [y/n] ? : ')

        if begin.lower() == 'n':
            print('So why launch the game ?')
            sys.exit()
        elif begin.lower() in ('y', ''):
            play = True
        else:
            begin = None
            print('Please enter "y" for yes or "n" for no.')

    # Main loop
    while play:
        # Set difficulty level
        level = input_int('level', '\nAt which level of difficulty do you want to play [1/2/3] ? : ')

        if level == 1:
            run = 15
            upper = 200
        elif level == 2:
            run = 10
            upper = 150
        else:
            run = 5
            upper = 100

        lev = f'You got {run} turn to find a number between 0 and {upper}'

        print('\n' + '_' * len(lev))
        print(lev + '\n' + '_' * len(lev))

        # Variable declaration
        turn = 0
        lower = 0
        win = False
        goal = random.randint(0, upper)

        # Game loop
        while turn < run and not win:
            choice = input_int('choice', f'Guess the number between {lower} and {upper} ? : ', upper, lower)

            turn += 1

            if choice == goal:
                win = True
            elif choice < goal:
                print(f'The number is greater than {choice}\n')
                lower = choice
            else:
                print(f'The number is minder than {choice}\n')
                upper = choice

        if win:
            print(f'Congratulation ! \nYou win in {turn} turn.\n')
        else:
            print(f'You loose ! \nThe number to find was {goal}.\n')

        again = None
        while again is None:
            again = input('Another game [y/n] ? : ')

            if again.lower() == 'n':
                print('\nSo sad ! See you next time !!')
                sys.exit()
            elif again.lower() in ('y', ''):
                play = True
            else:
                again = None
                print('Please enter "y" for yes or "n" for no.')


def input_int(setup, phrase, upper=None, lower=None):
    """Ask the user the phrase to declare the level or the choice.

    Input:
        - setup: level or choice
        - phrase: the phrase to be prompt
        - maxi: if level, the upper bound of the game
    """
    if setup == 'level':
        level = None
        while level is None:
            try:
                level = int(input(phrase))
                if level in (1, 2, 3):
                    return level
                else:
                    level = None
                    raise ValueError
            except ValueError:
                print('Select 1, 2 or 3.')
    elif setup == 'choice':
        choice = None
        while choice is None:
            try:
                choice = int(input(phrase))
                if lower <= choice <= upper:
                    return choice
                else:
                    choice = None
                    raise ValueError
            except ValueError:
                print(f'You must enter a number between 0 and {upper}')


if __name__ == '__main__':
    main()
