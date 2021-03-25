# input
N, M, x, y, K = map(int, input().split())
myMap = [list(map(int, input().split())) for _ in range(N)]
directions = list(map(int, input().split()))
                    # 동      서      북      남
direction = [[0,0], [0,1], [0,-1], [-1,0], [1,0]]
 
dicePos = [x,y]
dice = [0,0,0,0,0,0]

def checkOut(myDice):
  if myDice[0] < 0 or myDice[0] >= N or myDice[1] < 0 or myDice[1] >= M:
    return False
  return True

def rolling(myDirection):
  if myDirection == 1:
    newDice = [dice[4],dice[1],dice[0],dice[3],dice[5],dice[2]]
  elif myDirection == 2:
    newDice = [dice[2],dice[1],dice[5],dice[3],dice[0],dice[4]]
  elif myDirection == 3:
    newDice = [dice[3],dice[0],dice[2],dice[5],dice[4],dice[1]]
  else:
    newDice = [dice[1],dice[5],dice[2],dice[0],dice[4],dice[3]]
  return newDice

for direct in directions:
  if checkOut([dicePos[0]+direction[direct][0], dicePos[1]+direction[direct][1]]):
    dicePos[0] += direction[direct][0]
    dicePos[1] += direction[direct][1]
    dice = rolling(direct)
    if myMap[dicePos[0]][dicePos[1]] == 0:
      myMap[dicePos[0]][dicePos[1]] = dice[5]
    else:
      dice[5] = myMap[dicePos[0]][dicePos[1]]
      myMap[dicePos[0]][dicePos[1]] = 0
    print(dice[0])