from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def euclid_gcd(number1, number2):
    if number1 == 0:
        return number2
    elif number2 == 0:
        return number1
    elif number1 >= number2:
        return euclid_gcd(number1 % number2, number2)
    return euclid_gcd(number1, number2 % number1)


def play_round():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    value = f'{number1} {number2}'
    right_answer = euclid_gcd(number1, number2)
    return value, str(right_answer)
