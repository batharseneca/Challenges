''' CONFUSING EXPLANATION REDO LATER '''


input = '''X -/ X 5- 8/ 9- X 81 1- 4/X
62 71  X 9- 8/  X  X 35 72 5/8''' 
input = list((input).split("\n"))

gscores = []
lookup = {"-": 0,   }

for game in input:    
    for frame in game:    
        for ball in frame:
            if (ball.isspace() == False):
                gscores.append(ball)
    
    
    
    print gscores
    gscores = []
