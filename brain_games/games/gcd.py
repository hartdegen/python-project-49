from random import randint
from brain_games.cli import start_game


INFO_MESSAGE = "Find the greatest common divisor of given numbers."


def find_greatest_common_divisor(num1, num2):
    possible_divisor = num1
    while possible_divisor > 0:
        if (num1 % possible_divisor == 0) & (num2 % possible_divisor == 0):
            return possible_divisor
        possible_divisor -= 1
    return 1


def get_question_and_answer():
    value1 = randint(1, 100)
    value2 = randint(1, 100)
    question = f"Question: {value1} {value2}"
    answer = str(find_greatest_common_divisor(value1, value2))
    return (question, answer)


def start_game_brain_gcd():
    return start_game(INFO_MESSAGE, get_question_and_answer)
