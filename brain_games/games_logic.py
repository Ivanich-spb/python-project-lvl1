import prompt
from ansi.colour import fg
from brain_games.cli import welcome, welcome_user, congratulate_user, try_again


def start_game(game_name, number_of_rounds=3):
    welcome()
    print(game_name.GAME_RULES)
    print()
    name = welcome_user()

    count = 0
    while count < number_of_rounds:
        value, right_answer = game_name.game()
        print(f'Question: {value}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print(fg.green('Correct!'))
            count += 1
        else:
            print(f"'{fg.red(answer)}' is wrong answer ;(. Correct answer was '{fg.green(right_answer)}'.")# noqa E501
            try_again(name)
            break
    else:
        congratulate_user(name)
