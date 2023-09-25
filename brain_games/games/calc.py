from random import randint, choice
from brain_games.cli import start_game


INFO_MESSAGE = "What is the result of the expression?"
operations = ("+", "-", "*")


def get_question_and_answer():
    value1 = randint(1, 10)
    value2 = randint(1, 10)
    operation = choice(operations)
    question = f"Question: {value1} {operation} {value2}"
    answer = ""
    match operation:
        case "+":
            answer = str(value1 + value2)
        case "-":
            answer = str(value1 - value2)
        case "*":
            answer = str(value1 * value2)
        case _:
            raise ValueError("Unknown case !!!")
    return (question, answer)


def start_game_brain_calc():
    return start_game(INFO_MESSAGE, get_question_and_answer)
