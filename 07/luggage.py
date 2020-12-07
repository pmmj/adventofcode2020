import re

NO_BAGS = "no other bags"
COLOR_NAME_REGEX = re.compile(r'([a-z ]+) bags')
COLOR_CONTENTS_REGEX = re.compile(r'(\d+) ([a-z ]+) bags*')

def parseRules(rules):
    bagRules = {}
    for rule in rules:
        tokens = rule.split(" contain ")
        # print(tokens)
        color = re.match(COLOR_NAME_REGEX, tokens[0]).group(1)
        contents = tokens[1]
        if contents == NO_BAGS:
            bagRules[color] = None
        else:
            bagSplit = contents.split(", ")
            # print(bagSplit)
            typesOfBags = [re.match(COLOR_CONTENTS_REGEX, content).group(1, 2) for content in bagSplit]
            bagRules[color] = typesOfBags
    return bagRules

def searchForOuterBag(startColor, targetColor, bagRules):
    if startColor == targetColor:
        return 0
    visitedColors = {}
    queueColors = [startColor]
    while len(queueColors):
        color = queueColors.pop(0)
        colorsToVisit = bagRules[color]
        if colorsToVisit is not None:
            for (numberOfBags, colorToVisit) in colorsToVisit:
                if colorToVisit == targetColor:
                    return 1
                if colorToVisit not in visitedColors:
                    queueColors.append(colorToVisit)
        visitedColors[color] = 1
    return 0

def getAllBags(startColor, bagRules):
    amounts = bagRules[startColor]
    if amounts is None:
        return 0
    count = 0
    for (amountStr, color) in amounts:
        amount = int(amountStr)
        add = amount + amount * getAllBags(color, bagRules)
        count += add

    return count


with (open('input.txt', 'r')) as file:
    rules = [line.strip()[:-1] for line in file.readlines()]
    bagRules = parseRules(rules)
    # outerBags = [searchForOuterBag(color, "shiny gold", bagRules) for color in bagRules] 
    # print(sum(outerBags))
    counts = getAllBags("shiny gold", bagRules)
    print(counts)
