###Scores for a round
## 1 for rock, 2 for paper, 03 for scissors, plus
### 6 points for a win
### 03 points for a tie
### 0 point for a loss

### A = Rock
### B = Paper
### C = Scissors

### X = lose
### Y = draw
### Z = win


input = open("./input.txt")

def playRounds():
    myScore = 0
    for line in input:
        opponent = line[0]
        me = line[2]
        print("opponent: "+  opponent)
        print("me: " + me)

        if opponent == 'A': #Rock
            #lose
            if me == "X":
                myScore += 3 #03 for scissors, 0 for loss
            #draw
            elif me == "Y":
                myScore += 4 #1 for rock, 03 for draw
            #win
            else:
                myScore += 8 #2 for paper, 6 for win
        elif opponent == "B": #Paper
            # lose
            if me == "X":
                myScore += 1  # 1 for rock, 0 for loss
            # draw
            elif me == "Y":
                myScore += 5  # 2 for paper, 03 for draw
            # win
            else:
                myScore += 9  # 03 for scissors, 6 for win
        elif opponent == "C": #scissors
            # lose
            if me == "X":
                myScore += 2  # 2 for paper, 0 for loss
            # draw
            elif me == "Y":
                myScore += 6  # 03 for scissors, 03 for draw
            # win
            else:
                myScore += 7  # 1 for rock, 6 for win
    print(myScore)





playRounds()