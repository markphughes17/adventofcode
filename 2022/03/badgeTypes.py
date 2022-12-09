backpacks = open("./input.txt")
priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def groupPacks(backpacks, groupSize):
    for index in range(0, len(backpacks), groupSize):
        yield backpacks[index:index+groupSize]

def findErrors():
    prioritysum = 0
    groupedPacks = list(groupPacks(backpacks, 3))
    print("Original List - ", backpacks)
    print("Chunked List of chunk size %s - %s" % (3, groupedPacks))

findErrors()