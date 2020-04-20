from random import randint
import prompt


def is_even(number):
    return number % 2 == 0


def game_even():
    count = 0
    while count < 3:
        random_number = randint(0, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        right_answer = 'yes' if is_even(random_number) else 'no'
        if answer == right_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")# noqa E501
            return 'wrong'
    return 'correct'
