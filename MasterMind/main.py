""" The Master of the Mind """
import sys
from random import randint

RUN = 12
COLOR = ['green', 'yellow', 'red', 'blue', 'black']

def main():
    """The main function of the game"""
    print('### The Master of the Mind ! ###')
    print('# Can you read into the machine\'s brain ?\n')

    play = begin_game('Wanna try to master the Mind ? [y/n] : ', 'begin')

    while play:
        # Declare variable
        soluce = set_difficulty(COLOR)
        win = False
        turn = 0
        board = []

        while turn < RUN and not win:
            # Game loop
            turn += 1

            print('-' * len(f'Attempt {turn}/{RUN}'))
            print(f'Attempt {turn}/{RUN}')
            print('-' * len(f'Attempt {turn}/{RUN}'))

            answer = ask_answer(soluce, COLOR)

            board.append([answer, check_answer(answer, soluce)])

            print_board(board)

            if answer == soluce:
                win = True

        if win:
            print('\nYou WIN !!')
            print(f'Congratulation, you beat the computer mind in {turn} turns\n')
        else:
            print('You loose ...')
            print('Guess it\'s not for everyone to beat his own computer ...\n')

        # Exit or restart
        play = begin_game('Another game [y/n] ? : ', 'again')



def begin_game(phrase, setup):
    """Ask the user if he wants to play the game"""
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


def set_difficulty(color):
    """Ask the user for a difficulty level"""
    level = input_setup('level',
                        '\nAt which level of difficulty do you want to play [1/2/3] ? : '
                       ) + 3

    sol = []

    for _ in range(level):
        sol.append(color[randint(0, len(color) - 1)])

    print(f'You have {RUN} turn to find {len(sol)} colors')
    print('Let\'s begin ! \n')

    return sol


def input_setup(setup, phrase, color=None):
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
                choice = input(phrase)
                check = choice in color
                if not check:
                    choice = None
                    raise ValueError
            except ValueError:
                print(f'You must enter a color in {color}')

    return level if setup == 'level' else choice


def ask_answer(sol, color):
    """
    Ask the player for it's answer.

    Input:
        - sol: the list with the solution
        - color: the list containing possible color to pick
    Output:
        - answer: the answer of the player (list)
    """
    answer = []

    for unknown in range(len(sol)):
        unknown += 1
        choice = input_setup('choice', f'What\'s your guess for color {unknown} : ', color)

        answer.append(choice)

    print(f'\nYou bet on {answer}\n')

    return answer


def check_answer(answer, soluce):
    """Get the number of correct & misplaced colors
    Input :
        - soluce : the list of the solution
        - answer : the list containing the answer of the player
    Output:
        - response: a dict (see the declaration above)
    """
    response = {
        'Correct': 0,
        'Misplaced': 0
    }

    response['Correct'] = check_correct(soluce, answer)
    response['Misplaced'] = check_misplaced(soluce, answer) - response['Correct']


    return response


def check_correct(soluce, answer):
    """Get the number of correct placed colors"""
    return sum([answer[i] == soluce[i] for i in range(len(answer))])


def check_misplaced(soluce, answer):
    """
    Count the nb of color in the answer that are in the soluce.

    To have the number of misplaced, the nb of exact match must be substracted.
    """
    temp_sol = soluce.copy()
    misplaced = 0

    for i in answer:
        if i in temp_sol:
            temp_sol.remove(i)
            misplaced += 1

    return misplaced


def print_board(board):
    """
    Print all the attempt & their associate check into console

    Input:
        - board: a list containing :
            - the answer of the player
            - the check answer dict
    """
    for idx, attempt in enumerate(board):
        space = 0

        for color in attempt[0]:
            space += len(color)

        print(f'Trun {idx + 1} : ',
              attempt[0],
              ' ' * ((len(attempt[0]) * 6) - space),
              '- ',
              attempt[1]
             )


if __name__ == '__main__':
    main()
