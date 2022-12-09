
fullInventory = open("./inventory.txt", "r")


def printlines():
    initialInventory = fullInventory.readlines()
    formattedInventory = []
    totals = []
    for i in initialInventory:
        tempi = i.strip()
        formattedInventory.append(tempi)
    counter = 0
    for item in formattedInventory:
        if item == '':
            totals.append(counter)
            counter = 0
        else:
            counter += int(item)

    sortedTotals = sorted(totals, reverse=True)

    print("result: " + str(sum(sortedTotals[0:3])))


printlines()
