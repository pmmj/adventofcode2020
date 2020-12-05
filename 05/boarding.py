def findId(line):
    rowRange = (0, 127)
    colRange = (0, 7)
    # print(line)
    (rowSearch, finalRow, colSearch, finalCol) = (line[0:6], line[6], line[7:9], line[9])
    
    for half in rowSearch:
        if half == "F":
            rowRange = (rowRange[0], (rowRange[0] + rowRange[1]) // 2)
        else:
            rowRange = ((rowRange[0] + rowRange[1]) // 2 + 1, rowRange[1])
        print(rowRange)
    row = rowRange[0] if finalRow == "F" else rowRange[1]
    for half in colSearch:
        if half == "L":
            colRange = (colRange[0], (colRange[0] + colRange[1]) // 2)
        else:
            colRange = ((colRange[0] + colRange[1]) // 2 + 1, colRange[1])
        print(colRange)
    col = colRange[0] if finalCol == "L" else colRange[1]
    print(row, rowRange, col, colRange)
    return row * 8 + col

def loopForIds(ids):
    idTable = { id: True for id in ids }
    possibleSeats = []
    seatRange = range(min(ids), max(ids) + 1)
    for possibleId in seatRange:
        if possibleId not in idTable:
            print(possibleId, possibleId - 1 in idTable, possibleId + 1 in idTable)
            if possibleId - 1 in idTable and possibleId + 1 in idTable:
                possibleSeats.append((possibleId, possibleId - 1 in idTable, possibleId + 1 in idTable))
    return possibleSeats


# print(findId("FBFBBFFRLR"))
with (open('input.txt', 'r')) as file:
    lines = file.readlines()
    ids = [findId(line.strip()) for line in lines]
    # maxId = max(ids)
    # print(maxId)
    print(loopForIds(ids))
    