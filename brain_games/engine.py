from brain_games.cli import welcome_user


def engine(game, rounds=3):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(rounds):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(." 
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")