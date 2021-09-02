def check(x, y, board):
  now = board[x][y]
  right = board[x][y+1]
  bottom = board[x+1][y]
  diagonal = board[x+1][y+1]
  if now == right == bottom == diagonal:
    return True
  else:
    return False

def solution(m, n, board):
  answer = 0
  delete = [[0 for _ in range(n)] for _ in range(m)]
  for i in range(m):
    board[i] = list(board[i])

  # print()
  # for line in board:
  #   print(line)

  count = 1
  while count != 0:
    count = 0
    for i in range(m-1): # 행
      for j in range(n-1): # 열
        if board[i][j] != "X" and check(i, j, board) == True:
          delete[i][j], delete[i][j+1], delete[i+1][j], delete[i+1][j+1] = 1, 1, 1, 1

    # print()
    # for line in delete:
    #   print(line)
    
    for i in range(m): # 행
      for j in range(n): # 열
        if delete[i][j] == 1:
          board[i][j] = "X"
          delete[i][j] = 0
          count += 1
          answer += 1
    
    # print()
    # for line in board:
    #   print(line)


    for i in range(m-1, 1, -1):
      for j in range(n):
        if board[i][j] == "X":
          x = i-1
          while x >= 0 and board[x][j] == "X":
            x -= 1
          if x >= 0:
            board[i][j] = board[x][j]
            board[x][j] = "X"
    
  #   print()
  #   for line in board:
  #     print(line)

  #   print("-----------------------")
  # print(answer)
  return answer

solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])