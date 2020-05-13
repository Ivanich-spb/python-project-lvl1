import prompt
from ansi.colour import fg
from brain_games.cli import welcome, welcome_user, congratulate_user, try_again


def start_game(game, number_of_rounds=3):
    welcome()
    print(game.RULES)
    print()
    name = welcome_user()

    count = 0
    while count < number_of_rounds:
        value, right_answer = game.play_round()
        print(f'Question: {value}')
        answer = prompt.string('Your answer: ')
        if answer != right_answer:
            print(f"'{fg.bold(fg.red(answer))}' is wrong answer ;(. Correct answer was '{fg.bold(fg.green(right_answer))}'.")# noqa E501
            try_again(name)
            break
        print(fg.green('Correct!'))
        count += 1
    else:
        congratulate_user(name)
