input = open("./input.txt")



def compareassignments():
    lines = 0
    for line in input:
        pair = line.split(',')
        elf1 = pair[0].split('-')
        elf2 = pair[1].split('-')
        elf1range = set(range(int(elf1[0]), int(elf1[1])+1))
        elf2range = set(range(int(elf2[0]), int(elf2[1].strip('\n'))+1))
        if elf1range.issubset(elf2range) or elf2range.issubset(elf1range):
            lines +=1

    print("complete overlap: " + str(lines))

def totalAnyOverlaps():
    lines = 0
    input = open("./input.txt")
    for line in input:
        pair = line.split(',')
        elf1 = pair[0].split('-')
        elf2 = pair[1].split('-')
        elf1range = set(range(int(elf1[0]), int(elf1[1]) + 1))
        elf2range = set(range(int(elf2[0]), int(elf2[1].strip('\n')) + 1))
        if list(elf1range)[0] in elf2range or list(elf1range)[-1] in elf2range or list(elf2range)[0] in elf1range or list(elf2range)[-1] in elf1range:
            lines += 1




    print("Any overlap: " + str(lines))

compareassignments()
totalAnyOverlaps()