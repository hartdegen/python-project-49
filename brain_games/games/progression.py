from random import randint
from brain_games.cli import start_game


INFO_MESSAGE = 'What number is missing in the progression?'


def calculate_arithmetic_progression(start_value, difference, length=10):
    progression = []
    for i in range(length):
        progression.append(start_value + difference * i)
    return progression


def get_question_and_answer():
    init = randint(1, 100)
    step = randint(1, 10)
    random_index = randint(0, 9)
    progression = calculate_arithmetic_progression(init, step)
    answer = str(progression.pop(random_index))
    progression.insert(random_index, '..')
    question = "Question: " + " ".join((str(elem) for elem in progression))
    return (question, answer)


def start_game_brain_progression():
    return start_game(INFO_MESSAGE, get_question_and_answer)
