def find_block(now, board, block, visited, p):
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  for i in range(4):
    newX = now[0]+dx[i]
    newY = now[1]+dy[i]
    if 0 <= newX < len(board) and 0 <= newY < len(board):
      if board[newX][newY] == p and visited[newX][newY] == 0:
        block.append((newX, newY))
        visited[newX][newY] = 1
        find_block((newX,newY), board, block, visited, p)

def rotated(a):
  n = len(a)
  m = len(a[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]

  return result

def solution(game_board, table):
  answer = 0
  board_length = len(game_board)
  visited = [[0 for _ in range(board_length)] for _ in range(board_length)]
  spaces = []
  for i in range(board_length):
    for j in range(board_length):
      space = []
      if game_board[i][j] == 0 and visited[i][j] == 0:
        space.append((i,j))
        visited[i][j] = 1
        find_block((i,j), game_board, space, visited, 0)
      if len(space) != 0:
        spaces.append(space)

  visited = [[0 for _ in range(board_length)] for _ in range(board_length)]
  blocks = []
  for i in range(board_length):
    for j in range(board_length):
      block = []
      if table[i][j] == 1 and visited[i][j] == 0:
        block.append((i,j))
        visited[i][j] = 1
        find_block((i,j), table, block, visited, 1)
      if len(block) != 0:
        block.sort(key=lambda x: (x[0], x[1]))
        blocks.append(block)

  for block in blocks:
    for i in range(len(spaces)):
      if len(block) == len(spaces[i]) and len(block) == 2:
        answer += 2
        del spaces[i]
        break
      elif len(block) == len(spaces[i]):
        # block's x of first element is smallest
        # find the position based on the first block 
        template = [[0 for _ in range(board_length)] for _ in range(board_length)]
        for space in spaces[i]:
          template[space[0]][space[1]] = 1
        positions = [(0,0)]
        for j in range(1,len(block)):
          positions.append((block[j][0] - block[0][0], block[j][1] - block[0][1]))
        space = []
        for _ in range(4):
          flag = True
          for position in positions:
            if (spaces[i][0][0]+position[0], spaces[i][0][1]+position[1]) not in spaces[i]:
              flag = False
              break

          if flag == True: # 모든 위치가 일치
            answer += len(block)
            del spaces[i]
            break
          else: # 일치하지 않는 위치의 공간 존재
            space = []
            template = rotated(template) # rotate
            for j in range(len(template)):
              for k in range(len(template)):
                if template[j][k] == 1:
                  space.append((j,k))
            spaces[i] = space[:]
        if flag == True:
          break
  return answer

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
solution(game_board, table)