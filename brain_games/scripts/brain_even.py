#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user
from random import randint


MAX_ROUNDS = 3
INFO_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return True if number % 2 == 0 else False


def get_question_and_answer():
    random_number = randint(1, 100)
    question = f"Question: {random_number}"
    answer = "yes" if is_even(random_number) else "no"
    return (question, answer)


def start_game_brain_even():
    username = welcome_user()
    for _ in range(MAX_ROUNDS):
        question, answer = get_question_and_answer()
        print(INFO_MESSAGE)
        print(question)
        a = prompt.string("Your answer: ")
        if a == answer:
            print("Correct!")
        else:
            print(f"{a} is wrong answer ;(. Correct answer was {answer}")
            print(f"Let's try again, {username}!")
            return
    print(f"Congratulations, {username}!")


def main():
    start_game_brain_even()


if __name__ == "__main__":
    main()
