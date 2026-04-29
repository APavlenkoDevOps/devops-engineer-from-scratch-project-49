import random


def calcl_answer(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        
        
DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2}"
    correct_answer = calcl_answer(num1, num2, operator)
    return question, str(correct_answer)