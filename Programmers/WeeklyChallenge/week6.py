# 전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다. 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.
# 승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
# 자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.
# 자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.

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