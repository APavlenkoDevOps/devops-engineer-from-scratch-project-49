from brain_games.cli import welcome_user
from brain_games.even import even_check


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    even_check(name)


if __name__ == "__main__":
    main()