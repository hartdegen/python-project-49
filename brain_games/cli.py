import prompt


MAX_ROUNDS = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def start_game(info, get_question_and_answer):
    username = welcome_user()
    for _ in range(MAX_ROUNDS):
        question, answer = get_question_and_answer()
        print(info)
        print(question)
        response = prompt.string("Your answer: ")
        if response == answer:
            print("Correct!")
        else:
            print(f"{response} is wrong answer ;(. Correct answer was {answer}")
            print(f"Let's try again, {username}!")
            return
    print(f"Congratulations, {username}!")
