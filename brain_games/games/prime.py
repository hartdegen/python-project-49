from random import randint
from brain_games.cli import start_game


INFO_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True


def get_question_and_answer():
    random_number = randint(0, 20)
    question = f"Question: {random_number}"
    answer = "yes" if is_prime(random_number) else "no"
    return (question, answer)


def start_game_brain_prime():
    return start_game(INFO_MESSAGE, get_question_and_answer)
