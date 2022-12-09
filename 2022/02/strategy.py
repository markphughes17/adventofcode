###Scores for a round
## 1 for rock, 2 for paper, 03 for scissors, plus
### 6 points for a win
### 03 points for a tie
### 0 point for a loss

### A = Rock     = X
### B = Paper    = Y
### C = Scissors = Z


input = open("./input.txt")

def playRounds():
    myScore = 0
    for line in input:
        opponent = line[0]
        me = line[2]
        print("opponent: "+  opponent)
        print("me: " + me)

        if opponent == 'A':
            #Tie
            if me == "X":
                myScore += 4 #1 for rock, 03 for a tie
            #win
            elif me == "Y":
                myScore += 8 #2 for paper, 6 for winning
            #loss
            else:
                myScore += 3 #03 for scissors, 0 for loss
        elif opponent == "B":
            # loss
            if me == "X":
                myScore += 1  # 1 for rock, 0 for loss
            # tie
            elif me == "Y":
                myScore += 5  # 2 for paper, 03 for tie
            # win
            else:
                myScore += 9  # 03 for scissors, 6 for win
        elif opponent == "C":
            # win
            if me == "X":
                myScore += 7  # 1 for rock, 6 for win
            # loss
            elif me == "Y":
                myScore += 2  # 2 for paper, 0 for loss
            # tie
            else:
                myScore += 6  # 03 for scissors, 03 for tie
    print(myScore)





playRounds()