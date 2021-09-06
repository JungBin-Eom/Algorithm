def solution(weights, head2head):
  answer = []
  boxers = []
  for i in range(len(weights)):
    win = 0
    lose = 0
    winOver = 0
    for j in range(len(weights)):
      if i != j:
        if head2head[i][j] == 'W':
          win += 1
          if weights[i] < weights[j]:
            winOver += 1
        elif head2head[i][j] == 'L':
          lose += 1
    if win+lose != 0:
      winRate = win/(win+lose)
    else:
      winRate = 0
    boxers.append((winRate,winOver,weights[i],i+1))

  boxers = sorted(boxers, key=lambda x:(-x[0], -x[1], -x[2], x[3]))
  for boxer in boxers:
    answer.append(boxer[3])
  return answer

solution([145, 86, 86], ["NLW", "WNL", "LWN"])

# 15분