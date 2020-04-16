"""Greater_minder - The ultimate fun breaker"""
import sys
import random


def main():
    """Main function of the game"""
    print('### Greater-Minder - The ultimate fun breaker! ###')

    play = begin_game('Let\'s play the game [y/n] ? : ', 'begin')

    # Main loop
    while play:
        # Set difficulty level
        run, upper = set_difficulty()

        # Initial declaration
        turn = 0
        lower = 0
        win = False
        goal = random.randint(0, upper)

        # Game loop
        while turn < run and not win:
            choice = input_int(
                'choice',
                f'Guess the number between {lower} and {upper} ? : ',
                upper,
                lower
            )

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

        play = begin_game('Another game [y/n] ? : ', 'again')


def begin_game(phrase, setup):
    """Ask the user if he REALLY want to play at this lame game..."""
    begin = None
    while begin is None:
        begin = input(phrase)

        if begin.lower() == 'n':
            if setup == 'begin':
                print('So why launch the game ?')
            elif setup == 'again':
                print('\nSo sad ! See you next time !!')
            else:
                raise ValueError

            sys.exit()

        elif begin.lower() in ('y', ''):
            play = True
        else:
            begin = None
            print('Please enter "y" for yes or "n" for no.')

    return play


def set_difficulty():
    """Ask the user for a difficulty level"""
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

    return run, upper


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
                if level not in (1, 2, 3):
                    level = None
                    raise ValueError
            except ValueError:
                print('Select 1, 2 or 3.')
    elif setup == 'choice':
        choice = None
        while choice is None:
            try:
                choice = int(input(phrase))
                if not lower <= choice <= upper:
                    choice = None
                    raise ValueError
            except ValueError:
                print(f'You must enter a number between 0 and {upper}')

    return level if setup == 'level' else choice


if __name__ == '__main__':
    main()
