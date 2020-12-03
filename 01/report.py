import os

### Part 1
def report(inputs, target):
    table = {}
    for index in range(len(inputs)):
        input = inputs[index]
        if input not in table:
            table[input] = True

    for input in inputs:
        offset = target - input
        if offset in table:
            return [input, offset, input * offset]

with (open('input.txt', 'r')) as file:
    lines = file.readlines()
    values = [int(line.strip()) for line in lines]
    print(report(values, 2020))
