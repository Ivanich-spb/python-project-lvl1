from random import randint

RULES = 'What number is missing in the progression?'


def play_round():
    first_element = randint(0, 10)
    hidden_element = randint(0, 9)
    progression_step = randint(1, 10)
    progression = [
            str(i) for i in range(
                first_element,
                first_element + progression_step * 10,
                progression_step
                )
            ]
    right_answer = progression[hidden_element]
    progression[hidden_element] = '..'
    return ' '.join(progression), right_answer
