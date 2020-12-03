import functools
import re

def isValidPasswordOld(low, high, letter, password):
    count = password.count(letter)
    return low <= count and count <= high

def isValidPasswordNew(position1, position2, letter, password):
    firstLetter = password[position1 - 1]
    secondLetter = password[position2 - 1]
    return (firstLetter == letter or secondLetter == letter) and firstLetter != secondLetter


with (open('input.txt', 'r')) as file:
    lines = file.readlines()
    regex = re.compile(r"(\d+)-(\d+) (\w+): (\w+)")
    passwordValidators = [re.match(regex, line.strip()).group(1, 2, 3, 4) for line in lines]
    passwordValidations = [
        isValidPasswordNew(int(low), int(high), letter, password)
        for (low, high, letter, password) in passwordValidators
    ]
    numberOfCorrectPasswords = functools.reduce(lambda acc, cur: acc + 1 if cur else acc, passwordValidations, 0)
    print(numberOfCorrectPasswords)
