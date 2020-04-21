from random import randint


def is_prime(number):
    return number in [
            2, 3, 5, 7, 11,
            13, 17, 19, 23,
            29, 31, 37, 41,
            43, 47, 53, 59,
            61, 67, 71, 73,
            79, 83, 89, 97,
            ]


def game():
    random_num = randint(1, 99)
    answer = 'yes' if is_prime(random_num) else 'no'
    return random_num, answer


GAME_RULES = 'Answer "yes" if given number is PRIME. Otherwise answer "no".'
