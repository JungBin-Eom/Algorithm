def solution(stones, k):
  answer = 0
  while(True):
    answer += 1
    zeroStone = 0
    for i in range(len(stones)):
      if stones[i] != 0:
        stones[i] -= 1
    for i in range(len(stones)):
      if stones[i] == 0:
        zeroStone += 1
        if zeroStone == k: # 연속된 0 돌의 개수가 k개라면 끝
          return answer
      else:
        zeroStone = 0

stones = [10, 9, 8, 7, 5, 10, 100, 22]
k = 1
solution(stones, k)