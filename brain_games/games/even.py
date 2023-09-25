from random import randint
from brain_games.cli import start_game


INFO_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return True if number % 2 == 0 else False


def get_question_and_answer():
    random_number = randint(1, 100)
    question = f"Question: {random_number}"
    answer = "yes" if is_even(random_number) else "no"
    return (question, answer)


def start_game_brain_even():
    return start_game(INFO_MESSAGE, get_question_and_answer)
