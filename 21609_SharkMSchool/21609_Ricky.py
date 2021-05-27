N, M = map(int, input().split())
board = []
score = 0
moving = [(-1,0),(0,1),(1,0),(0,-1)] # 위쪽부터 시계방향
for _ in range(N):
  board.append(list(map(int, input().split(' '))))

for i in range(N):
  for j in range(N):
    board[i][j] = [board[i][j], False]

while True:
  # 블록 그룹 고르기
  groups = []
  for i in range(N):
    for j in range(N):
      if board[i][j][0] > 0 and board[i][j][1] == False:
        groupColor = board[i][j][0]
        visit = list()
        queue = list()
        queue.append((i,j))
        rainbowCount = 0

        while queue:
          block = queue.pop(0)
          if block not in visit:
            visit.append(block)
            if board[block[0]][block[1]][0] != 0:
              board[block[0]][block[1]][1] = True
            else:
              rainbowCount += 1
            for move in moving:
              newR = block[0]+move[0]
              newC = block[1]+move[1]
              if 0 <= newR < N and 0 <= newC < N and (newR, newC) not in visit and board[newR][newC][0] > -1:
                if board[newR][newC][0] == groupColor or board[newR][newC][0] == 0:
                  queue.append((newR,newC))

        visit.sort(key=lambda x:(x[0],x[1])) # visit[0]이 기준블록(0이면 그다음, 그다음)
        for block in visit:
          if board[block[0]][block[1]][0] != 0:
            stdBlock = block
            break
        
        if len(groups) == 0 and len(visit) > 1:
          groups.append([visit, rainbowCount, stdBlock])
        elif len(groups) != 0 and len(visit) > len(groups[0][0]):
          groups.clear()
          groups.append([visit, rainbowCount, stdBlock])
        elif len(groups) != 0 and len(visit) == len(groups[0][0]):
          groups.append([visit, rainbowCount, stdBlock])

  if len(groups) > 1:
    # print("정렬 전 group: ", groups)
    groups.sort(key=lambda group:(-group[1], -group[2][0], -group[2][1]))
    # print("정렬 후 group: ", groups)
  elif len(groups) == 0:
    print(score)
    exit()

  # print("make result=================")
  # for line in board:
  #   print(line)
  # print()

  # 블록 그룹 선택후 점수계산
  rmGroup = groups[0][0]
  score += len(rmGroup)**2
  for block in rmGroup:
    board[block[0]][block[1]][0] = -2

  # print("\n지우기 완료")
  # for line in board:
  #   print(line)
  # print()

  # 중력 작용
  for i in range(N-2, -1, -1):
    for j in range(N):
      if board[i][j][0] > -1:
        down = 1
        while i+down < N and board[i+down][j][0] == -2:
          down += 1
        temp = board[i][j]
        board[i][j] = board[i+down-1][j]
        board[i+down-1][j] = temp
  
  # print("\n중력 완료 1")
  # for line in board:
  #   print(line)
  # print()

  # 왼쪽으로 90도 회전
  rotate = [[0] * N for _ in range(N)]
  for r in range(N):
    for c in range(N):
      rotate[N-1-c][r] = board[r][c]
  board = rotate[:]

  # print("\n회전 완료")
  # for line in board:
  #   print(line)
  # print()

  # 중력 작용
  for i in range(N-2, -1, -1):
    for j in range(N):
      if board[i][j][0] > -1:
        down = 1
        while i+down < N and board[i+down][j][0] == -2:
          down += 1
        temp = board[i][j]
        board[i][j] = board[i+down-1][j]
        board[i+down-1][j] = temp

  # print("\n중력 완료2")
  # for line in board:
  #   print(line)
  # print()

  # 값 초기화
  for i in range(N):
    for j in range(N):
      board[i][j][1] = False

  # print("\n초기화 완료")
  # for line in board:
  #   print(line)
  # print()

  # print("지금까지의 score: ", score)