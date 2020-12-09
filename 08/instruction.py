import re
INSTRUCTION_REGEX = re.compile(r"((?:nop|acc|jmp)) ([\+\-]{1}\d+)")

def runProgram(instructions):
    indexesRan = {}
    currentInstruction = 0
    accumulator = 0
    while currentInstruction not in indexesRan and currentInstruction < len(instructions):
        indexesRan[currentInstruction] = True
        instruction = instructions[currentInstruction]
        (command, value) = re.match(INSTRUCTION_REGEX, instruction).group(1, 2)
        if command == "nop":
            currentInstruction += 1
        elif command == "jmp":
            currentInstruction += int(value)
        elif command == "acc":
            currentInstruction += 1
            accumulator += int(value)

    return accumulator, currentInstruction

def swapInstruction(instructions):
    n = len(instructions)
    for index in range(n):
        instruction = instructions[index]
        (command, value) = re.match(INSTRUCTION_REGEX, instruction).group(1, 2)
        if command == "nop" or command == "jmp":
            newValue = "jmp" if command == "nop" else "nop"
            newInstruction = f"{newValue} {value}"
            instructions[index] = newInstruction
            (acc, cur) = runProgram(instructions)
            if (cur >= n):
                return (acc, cur)
            instructions[index] = instruction

    return None, None

# def runProgramRecursively(
#     instructions,
#     indexesRan = {},
#     currentInstruction = 0,
#     swappedAt = None
#     ):
#     print(
#         currentInstruction, swappedAt
#     )
#     if currentInstruction == len(instructions):
#         return swappedAt

#     if currentInstruction not in indexesRan:
#         indexesRan[currentInstruction] = True
#         instruction = instructions[currentInstruction]
#         (command, value) = re.match(INSTRUCTION_REGEX, instruction).group(1, 2)
#         if command == "nop":
#             if swappedAt is None:
#                 swap = runProgramRecursively(instructions, indexesRan, currentInstruction + int(value), currentInstruction)
#                 if swap is not None:
#                     return swap
#             return runProgramRecursively(instructions, indexesRan, currentInstruction + 1, swappedAt)
#         elif command == "jmp":
#             if swappedAt is None:
#                 swap = runProgramRecursively(instructions, indexesRan, currentInstruction + 1, currentInstruction)
#                 if swap is not None:
#                     return swap
#             return runProgramRecursively(instructions, indexesRan, currentInstruction + int(value), swappedAt)
#         elif command == "acc":
#             return runProgramRecursively(instructions, indexesRan, currentInstruction + 1, swappedAt)
#     else:
#         return None


with (open('input.txt', 'r')) as file:
    instructions = [line.strip() for line in file.readlines()]
    # acc = runProgram(instructions)
    changeInstruction = swapInstruction(instructions)
    print(changeInstruction)