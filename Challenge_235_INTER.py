''' COMPLETED PYTHONIC SOLUTION '''


input = '''X -/ X 5- 8/ 9- X 81 1- 4/X
62 71  X 9- 8/  X  X 35 72 5/8''' 
input = list((input).split("\n"))

gscores = []
gamecount = 1

for game in input:    
    for frame in game:    
        for ball in frame:
            if (ball.isspace() == False):
                gscores.append(ball)
    
    score = 0
    for i in range(len(gscores)):
        if gscores[i] == 'X':
            gscores[i] = 10
        elif gscores[i] == '-':
            gscores[i] = 0
        elif gscores[i] == '/':
            continue
        else:
            gscores[i] = int(gscores[i])

    for x in range(len(gscores)):
        ball = gscores[x]
        if len(gscores) - 3 <= x:
            if ball == '/':
                score += (10 - gscores[x-1])
            else:
                score += ball
            continue
        elif ball == 10:
            score += ball
            score += gscores[x+1]
            if gscores[x+2] == '/':
                score += (10 - gscores[x+1])
            else:
                score += gscores[x+2]
        elif ball == '/':
            score += (10 - gscores[x-1])
            score += gscores[x+1]
        else:
            score += ball

    print "The Score For Game: " + str(gamecount) + " Is " + str(score)    
    gscores = []
    gamecount = gamecount + 1
