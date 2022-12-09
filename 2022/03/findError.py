backpacks = open("./input.txt")
priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def finderrors():
    list_of_groups = list(zip(*(iter(backpacks),) * 3))
    prioritySum = 0
    for group in list_of_groups:
        bag1 = group[0]
        bag2 = group[1]
        bag3 = group[2]
        for char in bag1:
            if char in bag2 and char in bag3:
                priority = priorities.index(char)+1
                prioritySum += priority
                break

    print(prioritySum)


finderrors()