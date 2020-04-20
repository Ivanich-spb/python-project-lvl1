#! /usr/bin/env python3

from brain_games.cli import welcome_user, congratulate_user, try_again
from brain_games.games_rules import brain_even_rules
from brain_games.scripts.brain_games import welcome
from brain_games.games_logic import game_even


def main():
    welcome()
    brain_even_rules()
    print()
    name = welcome_user()
    result = game_even()
    if result == 'correct':
        congratulate_user(name)
    else:
        try_again(name)


if __name__ == '__main__':
    main()
