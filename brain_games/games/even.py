from random import randint


def is_even(number):
    return number % 2 == 0


def game():
    random_number = randint(0, 100)
    right_answer = 'yes' if is_even(random_number) else 'no'
    return random_number, right_answer


GAME_RULES = 'Answer "yes" if number EVEN otherwise answer "no".'
