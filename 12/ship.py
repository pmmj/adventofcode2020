# I MESSED UP THE NAMES
# FIRST FUNCTION NAME IS SOLUTION 1's NAME BUT I MESSED UP LMFAO
# LEAVING IT LIKE THIS FOR HONESTY

NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"
LEFT = "L"
RIGHT = "R"
FORWARD = "F"

def calculateShipDistance(directions):
    x = 0
    y = 0
    wx = 10
    wy = 1
    moves = [(direction[0], int(direction[1:])) for direction in directions]
    for (d, delta) in moves:
        if d == NORTH:
            wy += delta
        elif d == EAST:
            wx += delta
        elif d == SOUTH:
            wy -= delta
        elif d == WEST:
            wx -= delta
        elif d == LEFT:
            turns = delta // 90
            for i in range(turns):
                temp = wx
                wx = -wy
                wy = temp
        elif d == RIGHT:
            turns = delta // 90
            for i in range(turns):
                temp = wx
                wx = wy
                wy = -temp
        elif d == FORWARD:
            for i in range(delta):
                x += wx
                y += wy

    return (x, y, abs(x) + abs(y))

def calculateWaypointDistance(directions):
    x = 0
    y = 0
    curDir = 0
    moves = [(direction[0], int(direction[1:])) for direction in directions]
    for (d, delta) in moves:
        if d == NORTH:
            y += delta
        elif d == EAST:
            x += delta
        elif d == SOUTH:
            y -= delta
        elif d == WEST:
            x -= delta
        elif d == LEFT:
            curDir = (curDir + delta) % 360
        elif d == RIGHT:
            curDir = (curDir - delta) % 360
        elif d == FORWARD:
            if curDir == 0:
                x += delta
            elif curDir == 90:
                y += delta
            elif curDir == 180:
                x -= delta
            else:
                y -= delta

    return (x, y, abs(x) + abs(y))

with (open('input.txt', 'r')) as file:
    directions = [line.strip() for line in file.readlines()]
    print(calculateShipDistance(directions))