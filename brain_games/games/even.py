from random import randint

RULES = 'Answer "yes" if number EVEN otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def play_round():
    random_number = randint(0, 100)
    right_answer = 'yes' if is_even(random_number) else 'no'
    return random_number, right_answer
