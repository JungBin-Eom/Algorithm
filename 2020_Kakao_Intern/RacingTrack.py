N = 0
answer = 99999999

def dfs(board, point, direction, cost, visited):
  global answer

  if point[0] == N-1 and point[1] == N-1:
    # print()
    # print("arrive at finish point")
    # print("now cost: ", cost)
    # print("now answer: ", answer)
    # print()
    if cost < answer:
      answer = cost
    return

  moves = [[-1,0,'u'],[0,1,'r'],[1,0,'d'],[0,-1,'l']] # 상 우 하 좌

  for move in moves:
    nextPoint = (point[0]+move[0], point[1]+move[1])
    if (0 <= nextPoint[0] < N and 0 <= nextPoint[1] < N) and board[nextPoint[0]][nextPoint[1]] == 0:
      
      nextCost = cost
      if point[0] == 0 and point[1] == 0:
        nextCost += 100
      elif direction == move[2]:
        nextCost += 100
      else:
        nextCost += 600

      if nextPoint not in visited or nextCost <= visited[nextPoint]:
        visited[nextPoint] = nextCost
        dfs(board, nextPoint, move[2], nextCost, visited)

def solution(board):
  global N
  N = len(board)
  visited = {(0,0):0}

  start = (0,0)
  visited[start] = 0
  dfs(board, start, 'x', 0, visited)

  return answer