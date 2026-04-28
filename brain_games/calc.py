from brain_games.cli import name_input
import random

def calcl_answer(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2

def calc(name=None):
    if not name:
        name = name_input()
    print("What is the result of the expression?")
    counter = 0
    while counter < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        print(f'Question: {num1} {operator} {num2}')
        correct_answer = calcl_answer(num1, num2, operator)
        answer = input('Your answer: ')
        if answer == str(correct_answer):
            print(f'Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again! '{name}'")
            break
    else:
        print(f"Congratulations, {name}!")