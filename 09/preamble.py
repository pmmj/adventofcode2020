def handlePreamble(numbers):
    # preamble = { number: True for number in numbers[:25] }
    # checks = numbers[25:]
    for i in range(25, len(numbers)):
        print(f"~~~{i}~~~")
        value = numbers[i]
        checks = { number: True for number in numbers[i-25:i] }
        print(checks)
        isValid = False
        for check in checks:
            offset = value - check
            print(offset)
            if offset in checks:
                isValid = True
                break
        if not isValid:
            return value
    return None

def contiguousSet(numbers, target):
    for i in range(len(numbers)):
        count = numbers[i]
        s = [numbers[i]]
        for j in range (i + 1, len(numbers)):
            count += numbers[j]
            s.append(numbers[j])
            if count == target:
                return (min(s), max(s), min(s) + max(s))

    return None


with (open('input.txt', 'r')) as file:
    numbers = [int(line.strip()) for line in file.readlines()]
    target = handlePreamble(numbers)
    print(target)
    s = contiguousSet(numbers, target)
    print(s)