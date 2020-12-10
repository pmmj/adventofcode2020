# def findLongestChain(adapters, visitedAdapters = {}, path = []):
#     print(path, visitedAdapters)
#     if len(path) == len(adapters):
#         return path

#     lastAdapter = 0 if len(path) == 0 else path[-1]
#     for adapter in adapters:
#         if adapter not in visitedAdapters and adapter > lastAdapter and adapter - lastAdapter <= 3:
#             visitedAdapters[adapter] = True
#             path.append(adapter)
#             chain = findLongestChain(adapters, visitedAdapters, path)
#             if chain:
#                 return chain
#             path.pop()
#             visitedAdapters.pop(adapter, None)
#     return None

# def getNumberOfPossibleChains(chain, offset = 0):
#     print(offset)
#     if offset == len(chain) - 2:
#         return 1

#     diff = chain[offset + 2] - chain[offset]
#     if diff <= 3:
#         removedAdapter = chain.pop(offset + 1)
#         numberWithoutAdapter = getNumberOfPossibleChains(chain, offset + 1)
#         chain.insert(offset + 1, removedAdapter)
#         numberWithAdapter = getNumberOfPossibleChains(chain, offset + 1)
#         return numberWithAdapter + numberWithoutAdapter
        
#     return getNumberOfPossibleChains(chain, offset + 1)

def createReverseDagFromChain(chain):
    dag = { node: [] for node in chain }
    dag[0] = []
    dag[max(chain) + 3] = []
    # could optimize but IDC
    for u in dag:
        for v in dag:
            diff = v - u
            if diff <= 3 and diff > 0:
                dag[v].append(u)

    return dag

def countPathsInDag(dag, chain, start, target):
    newChain = chain[::-1]
    newChain.insert(0, start)
    newChain.append(target)

    count = { node: 0 for node in newChain }
    count[start] = len(dag[start])

    for node in newChain:
        neighbourhood = dag[node]
        for neighbour in neighbourhood:
            count[neighbour] += count[node]

    return count[target]


def getDifferences(chain):
    count1 = 1
    count3 = 1
    for i in range(1, len(chain)):
        diff = chain[i] - chain[i - 1]
        if diff == 1:
            count1 += 1
        elif diff == 3:
            count3 += 1

    return (count1, count3, count1 * count3)



with (open('input.txt', 'r')) as file:
    adapters = [int(line.strip()) for line in file.readlines()]

    # chain = findLongestChain(adapters)
    chain = sorted(adapters)
    print(chain)
    dag = createReverseDagFromChain(chain)
    print(dag)
    print(countPathsInDag(dag, chain, max(chain) + 3, 0))
