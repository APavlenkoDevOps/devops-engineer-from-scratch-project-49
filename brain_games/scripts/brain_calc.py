from brain_games.calc import calc
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    calc(name)

if __name__ == "__main__":
    main()