#! /usr/bin/env/ python3
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print()
    return name


def congratulate_user(name):
    print(f'Congratulations, {name}!')


def try_again(name):
    print(f"Let's try again, {name}!")
