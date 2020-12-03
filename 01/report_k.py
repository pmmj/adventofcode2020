def report(inputs, target, numberOfInputs):
    report = report_helper(inputs, target, numberOfInputs, 0, table, [])


def report_helper(inputs, target, numberOfInputs, runningSum, table, path):
    if numberOfInputs == 1:
        offset = target - runningSum
        if offset in table:
            return path + [offset]
        else:
            return None
    else:
        for input in inputs:
            if input not in path:
                path.append(input)
                newPath = report_helper(inputs, target, numberOfInputs - 1, runningSum + input, table, path)
                if newPath is not None:
                    return newPath
                else:
                    path.pop()
        return None

with (open('input.txt', 'r')) as file:
    lines = file.readlines()
    values = [int(line.strip()) for line in lines]
    print(report(values, 2020, 3))
   