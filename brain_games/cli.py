#! /usr/bin/env/ python3
import prompt
from ansi.colour import fg


def welcome():
    print(fg.bold('Welcome to the Brain Games!'))


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {fg.bold(name)}!')
    print()
    return name


def congratulate_user(name):
    print(fg.green(f'Congratulations, {fg.bold(name)}!'))


def try_again(name):
    print(f"Let's try again, {fg.bold(name)}!")
