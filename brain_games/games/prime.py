from random import randint

RULES = 'Answer "yes" if given number is PRIME. Otherwise answer "no".'


def is_prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return count == 2


def play_round():
    random_number = randint(0, 100)
    right_answer = 'yes' if is_prime(random_number) else 'no'
    return random_number, right_answer
