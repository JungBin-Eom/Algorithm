N, K = map(int, input().split())
A = list(map(int, input().split()))
belt = [0 for _ in range(N)]
step = 0

while True:
  step += 1

  # first step
  A = [A[len(A)-1]] + A[:len(A)-1] # 벨트 한칸 이동
  belt = [0] + belt[:len(belt)-1]
  belt[N-1] = 0 # 내리는 위치 로봇 내림

  # second step
  i = N-1
  for robot in belt[::-1]:
    if robot == 1: # 로봇 있음
      if i != N-1 and belt[i+1] == 0 and A[i+1] >= 1:
        belt[i+1] = 1
        belt[i] = 0
        A[i+1] -= 1
    i -= 1

  # third step
  if A[0] != 0:
    A[0] -= 1 
    belt[0] = 1 # 올리는 위치에서 로봇올리기
  
  # forth step
  zero = 0
  for power in A:
    if power == 0:
      zero += 1
    if zero >= K:
      print(step)
      exit()
