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

        while turn < RUN and not win:
            # Game loop
            turn += 1

            print('-' * len(f'Attempt {turn}/{RUN}'))
            print(f'Attempt {turn}/{RUN}')
            print('-' * len(f'Attempt {turn}/{RUN}'))

            answer = ask_answer(soluce, COLOR)
            
            print(answer, check_answer(answer, soluce))

            #TODO: print the board game : answer 1 - reponse 1 \n answer 2 - response 2
                #TODO: get the answer in board
                #TODO: get the response in board

            if answer == soluce:
                win = True
        
        if win:
            print('You win !!')
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
    level = input_setup('level', '\nAt which level of difficulty do you want to play [1/2/3] ? : ') + 3

    sol = []

    for x in range(level):
        sol.append(color[randint(0, len(color) - 1)])

    print(f'You have {RUN} turn to find {len(sol)} colors')
    print('Let\'s begin ! \n')

    return sol


def input_setup(setup, phrase, color=None):  #TODO: MasterMind it
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
    answer = []

    for unknown in range(len(sol)):
        unknown += 1
        choice = input_setup('choice', f'What\'s your guess for color {unknown} : ', color)

        answer.append(choice)

    print(f'\nYou bet on {answer}\n')
    
    return answer


def check_answer(answer, soluce):  #FIXME: problem if 2 times the same color
    temp_soluce = soluce.copy()
    response = {
        'Correct': 0,
        'Misplaced': 0,
        'Inexistant': 0
    }
    
    for i, ans in enumerate(answer):
        if ans == soluce[i]:
            response['Correct'] += 1
            temp_soluce.remove(ans)
        elif ans in temp_soluce:
            response['Misplaced'] += 1
        else:
            response['Inexistant'] += 1

    return response


if __name__ == '__main__':
    main()
