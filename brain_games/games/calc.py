from random import randint, choice
from operator import mul, add, sub

RULES = 'What is the result of the expression?'
OPERATORS = [
    ('*', mul),
    ('-', sub),
    ('+', add),
]


def play_round():
    operator = choice(OPERATORS)
    operand1 = randint(0, 100)
    operand2 = randint(0, 100)
    value = f'{operand1} {operator[0]} {operand2}'
    right_answer = operator[1](operand1, operand2)
    return value, str(right_answer)
