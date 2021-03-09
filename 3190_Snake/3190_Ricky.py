# input
N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
rotations = [list(input().split()) for _ in range(L)]

# 행, 열, 방향(0:위, 1:오, 2:아래, 3:왼)
snake = [1, 1, 1]
snakes = [[1,1]]
time = 1
directions = [[-1,0], [0,1], [1,0], [0,-1]]

# 지도에 뱀과 사과의 위치 넣음
myMap = [[0 for _ in range(N+1)] for _ in range(N+1)]
myMap[1][1] = 1
for apple in apples:
  myMap[apple[0]][apple[1]] = 2

while(time):
  # print(time, snakes, snake)
  # 이동
  snake[0] += directions[snake[2]][0] # 행
  snake[1] += directions[snake[2]][1] # 열
  if snake[0] > N or snake[0] < 1 or snake[1] > N or snake[1] < 1: # 벽에 박음
    break
  elif myMap[snake[0]][snake[1]] == 1: # 몸에 박음
    break
  else:
    snakes.append([snake[0], snake[1]])

  # 사과 찾기
  if myMap[snake[0]][snake[1]] == 2: # 사과 찾음
    myMap[snake[0]][snake[1]] = 1
  else: # 빈칸(1인 경우는 위에서 걸러냄)
    myMap[snake[0]][snake[1]] = 1
    myMap[snakes[0][0]][snakes[0][1]] = 0
    snakes = snakes[1:]
      
  # 회전
  if len(rotations) != 0:
    if time == int(rotations[0][0]):
      # print("회전!")
      if rotations[0][1] == 'L':
        snake[2] -= 1
        if snake[2] == -1:
          snake[2] = 3
      else:
        snake[2] += 1
        if snake[2] == 4:
          snake[2] = 0
      rotations = rotations[1:]

  time += 1

print(time)