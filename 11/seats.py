EMPTY_SEAT = "L"
FLOOR = "."
OCCUPIED_SEAT = "#"

def getSeatsState(seats):
    return {
        (i, j): seats[i][j] for i in range(len(seats)) for j in range(len(seats[i]))
    }

def countAdjacentSeats(state, position):
    (i, j) = position
    floor = 0
    occupied = 0
    empty = 0
    positions = [
        (i + 1, j + 1),
        (i + 1, j),
        (i + 1, j - 1),
        (i - 1, j + 1),
        (i - 1, j),
        (i - 1, j - 1),
        (i, j + 1),
        (i, j - 1),
    ]
    for position in positions:
        if position in state:
            seat = state[position]
            if seat == EMPTY_SEAT:
                empty += 1
            elif seat == FLOOR:
                floor += 1
            else:
                occupied += 1

    return (empty, occupied, floor)

def getOldChange(state, position):
    seat = state[position]
    newSeat = seat
    change = 0
    [empty, occupied, floor] = countAdjacentSeats(state, position)
    if seat == EMPTY_SEAT and occupied == 0:
        newSeat = OCCUPIED_SEAT
        change = 1
    elif seat == OCCUPIED_SEAT and occupied >= 4:
        newSeat = EMPTY_SEAT
        change = 1
    return (newSeat, change)

def countSeatsInLine(state, position):
    (i, j) = position
    floor = 0
    occupied = 0
    empty = 0
    directions = [
        (1, 1),
        (1, 0),
        (1, -1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, 1),
        (0, -1),
    ]
    for direction in directions:
        (xd, yd) = direction
        (i, j) = position
        newPosition = (i + xd, j + yd)
        newSeat = None
        while newPosition in state and newSeat is None:
            seat = state[newPosition]
            if seat == EMPTY_SEAT or seat == OCCUPIED_SEAT:
                newSeat = seat
            else:
                (i, j) = newPosition
                newPosition = (i + xd, j + yd)
        if newSeat:
            if newSeat == OCCUPIED_SEAT:
                occupied += 1
            elif newSeat == EMPTY_SEAT:
                empty += 1
        else:
            floor += 1

    return (empty, occupied, floor)

def getNewChange(state, position):
    seat = state[position]
    newSeat = seat
    change = 0
    [empty, occupied, floor] = countSeatsInLine(state, position)
    if seat == EMPTY_SEAT and occupied == 0:
        newSeat = OCCUPIED_SEAT
        change = 1
    elif seat == OCCUPIED_SEAT and occupied >= 5:
        newSeat = EMPTY_SEAT
        change = 1
    return (newSeat, change)

def modelSeats(seats):

    initialState = getSeatsState(seats)
    changes = None
    state = initialState
    # print(state)
    while changes != 0:
        newState = {}
        changes = 0
        sameState = True
        for position in state:
            # (newSeat, change) = getOldChange(state, position)
            (newSeat, change) = getNewChange(state, position)
            newState[position] = newSeat
            changes += change
        state = newState

    # print("done")
    count = 0
    # print(state)
    for position in state:
        if state[position] == OCCUPIED_SEAT:
            count += 1

    return count
    



# with (open('input.txt', 'r')) as file:
with (open('input.txt', 'r')) as file:
    seats = [line.strip() for line in file.readlines()]
    print(modelSeats(seats))