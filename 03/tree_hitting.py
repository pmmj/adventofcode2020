import functools
TREE_SQUARE = "#"

def count_trees_on_line(treelines, numberOfSquaresToRepeat, v, h, vDelta, hDelta):
    numberOfTreelines = len(treelines)
    currentHPosition = (h + hDelta) % numberOfSquaresToRepeat
    currentVPosition = v + vDelta
    numberOfTreesInTheWay = 0
    while currentVPosition < numberOfTreelines:
        currentPositionState = treelines[currentVPosition][currentHPosition]
        if currentPositionState == TREE_SQUARE:
            numberOfTreesInTheWay += 1
        currentHPosition = (currentHPosition + hDelta) % numberOfSquaresToRepeat
        currentVPosition = currentVPosition + vDelta

    return numberOfTreesInTheWay

with (open('input.txt', 'r')) as file:
    lines = file.readlines()
    treelines = [line.strip() for line in lines]
    slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    treesPerSlope = [
        count_trees_on_line(treelines, len(treelines[0]), 0, 0, v, h)
        for (v, h) in slopes
    ]
    productOfTrees = functools.reduce(lambda acc, cur: acc * cur, treesPerSlope)
    print(productOfTrees)