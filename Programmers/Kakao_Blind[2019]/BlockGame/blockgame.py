def solution(board):
  answer = 0

  # blockType = [
  #   [(0,1),(0,2),(1,2)],[(0,1),(1,0),(2,0)],[(1,0),(1,1),(1,2)],[(1,0),(2,0),(2,-1)],
  #   [(0,1),(0,2),(1,0)],[(1,0),(2,0),(2,1)],[(1,-2),(1,-2),(1,0)],[(0,1),(1,1),(2,1)],
  #   [(1,-1),(1,0),(1,1)],[(1,0),(2,0),(1,1)],[(0,1),(0,2),(1,1)],[(1,0),(2,0),(1,-1)]]

  blockType = [
    [(1,0),(1,1),(1,2)],[(1,0),(2,0),(2,-1)],
    [(1,0),(2,0),(2,1)],[(1,-2),(1,-1),(1,0)],
    [(1,-1),(1,0),(1,1)]]
  
  fill = [
    [(0,1),(0,2)],[(0,-1),(1,-1)],
    [(0,1),(1,1)],[(0,-2),(0,-1)],
    [(0,-1),(0,1)]
  ]

  boardLen = len(board)
  delete = 999999
  while delete != 0:
    delete = 0
    for i in range(boardLen):
      for j in range(boardLen):
        if board[i][j] != 0:
          btype = 0
          for block in blockType:
            match = 0
            for next in block:
              nextX, nextY = i+next[0], j+next[1]
              if 0 <= nextX < boardLen and 0 <= nextY < boardLen and board[nextX][nextY] == board[i][j]:
                match += 1
            if match == 3:
              btype = blockType.index(block)
              print(i, j, btype)
              blocked = False
              for k in range(i+fill[btype][0][0]+1):
                if board[k][j+fill[btype][0][1]] != 0:
                  blocked = True
                  break
              if blocked == False:
                for l in range(i+fill[btype][1][0]+1):
                  if board[l][j+fill[btype][1][1]] != 0:
                    blocked = True
                    break
                if blocked == False:
                  answer += 1
                  delete += 1
                  board[i][j] = 0
                  for next in blockType[btype]:
                    board[i+next[0]][j+next[1]] = 0
              for line in board:
                print(line)
              print()
              break

        
  print(answer)
  return answer

solution([
  [1,2,2,2,3,3,0,0,8,9],
  [1,1,1,2,3,0,8,8,8,9],
  [0,0,0,0,3,0,0,0,9,9],
  [0,0,0,0,0,2,0,0,0,0],
  [7,0,0,0,2,2,2,0,0,0],
  [7,0,0,0,0,0,0,0,0,0],
  [7,7,6,0,3,0,0,0,0,0],
  [6,6,6,2,3,0,4,0,0,5],
  [1,2,2,2,3,3,4,4,4,5],
  [1,1,1,0,0,0,0,0,5,5]])

# 1시간 17분
# 블록이 겹쳐잇는 경우 생각하는게 어려웠음
# 예시)
# [1,0,2,2,2,0]
# [1,1,1,0,2,0]
# [0,0,0,0,0,0]
# [0,0,0,0,0,0]
# [0,0,0,0,0,0]
# [0,0,0,0,0,0]
# 이 경우 2번 먼저 지우고 1번을 지워야 하는데 기존 풀이로는 무조건 1번부터 보고 지우게돔
# 2번의 경우 못지우는 블록이므로 결과적으로 1번도 못지움