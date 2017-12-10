# Homework 9

## Add "Enemy Goal" to ***GreeyEater*** game

## Requirements:
### 1. Remix the game code from this link: https://trinket.io/python/bc97df6f83

### 2. Extend the game to have some "Enemy Goals". The differences between "Enemy Goal" and normal goal are:

2.1 "Enemy Goal" is in shape of "triangle" (***Hint***: turtle has "triangle" shape) instead of "circle".

2.2 When "Enemy Goal" is hit by player, the score should be decreased(not increased) by "1". So player should avoid to hit "Enemy Goal".

### 3: A few hints:
3.1 Try create a new class for "Enemy Goal".

3.2 Try use inheritance to avoid duplicating code. 

3.3 The main program should something like this:

```
# Main Program
myGame = GreedyEater()

myGame.createStage(400, "Yellow")

myGame.addPlayer("turtle", "Red")

myGame.addGoals(20, "Blue")

# Add Enemy Goals!
myGame.addEnemyGoals(10, "Green")

myGame.start()
```

3.4 The final result should be like this:
<iframe src="https://trinket.io/embed/python/ecccdaf56d?outputOnly=true&start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### 4. Reply the homework post on google class room with your remixed code link.

