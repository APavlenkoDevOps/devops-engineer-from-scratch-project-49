import random

from brain_games.cli import name_input


def start():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")


def is_even(num):
    return num % 2 == 0


def even_check(name=None):
    start()
    if not name:
        name = name_input()
    counter = 0
    while counter < 3:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        correct_answer = 'yes' if is_even(num) else 'no'
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print("Let's try again!")
            break
    else:
        print(f'Congratulations, {name}!')