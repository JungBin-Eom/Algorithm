def solution(stones, k):
  answer = 0
  # 니니즈 친구들은 최소 1명 ~ 최대 2억명
  # 범위를 줄여나가면서 binary search
  # 2억명인 경우 단순 배열 탐색으로 풀면 시간이 굉장히 많이 소요됨
  begin = 1
  end = 200000000
  while begin <= end:
    tmpStones = stones[:]
    zeroStone = 0 # 연속된 0돌의 개수
    mid = (begin + end) // 2 # 중간값
    for i in range(len(tmpStones)):
      tmpStones[i] -= mid
      if tmpStones[i] <= 0:
        zeroStone += 1
        if zeroStone >= k:
          break
      else:
        zeroStone = 0 
    if zeroStone >= k:
      end = mid - 1
    else:
      begin = mid + 1
  return begin