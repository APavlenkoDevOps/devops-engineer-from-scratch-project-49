import prompt


def name_input():
    name = prompt.string('May I have your name? ')
    return name


def welcome_user():
    name = name_input()
    print(f'Hello, {name}!')
    return name