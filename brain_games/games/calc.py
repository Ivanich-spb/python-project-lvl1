from random import randint, choice


def game():
    operator = choice(['+', '-', '*'])
    operand1 = randint(0, 100)
    operand2 = randint(0, 100)
    value = f'{operand1} {operator} {operand2}'
    right_answer = eval(value)
    return value, str(right_answer)


GAME_RULES = 'What is the result of the expression?'
