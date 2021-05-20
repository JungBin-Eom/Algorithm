N = int(input())
classRoom = [[0 for _ in range(N)] for _ in range(N)]
students = {}
moves = [(-1,0), (0,1), (1,0), (0,-1)] # 위-오-아-왼(시계방향)
result = 0

for _ in range(N*N):
  stud = list(map(int, input().split(' ')))
  students[stud[0]] = stud[1:5]

for student, likes in students.items():
  candidate = []
  for i in range(N):
    for j in range(N):
      like, empty = 0, 0
      if classRoom[i][j] == 0: # 빈자리
        for move in moves:
          if 0 <= i+move[0] < N and 0 <= j+move[1] < N:
            if classRoom[i+move[0]][j+move[1]] in likes:
              like += 1
            elif classRoom[i+move[0]][j+move[1]] == 0:
              empty += 1
        candidate.append([like, empty, N-i, N-j]) # 인접 자리에 좋아하는 학생 수, 빈자리 수, row, col
  candidate.sort()
  selected = candidate[-1]
  classRoom[abs(selected[2]-N)][abs(selected[3]-N)] = student
  # print(classRoom)

for i in range(N):
  for j in range(N):
    count = 0
    for move in moves:
      if 0 <= i+move[0] < N and 0 <= j+move[1] < N:
        if classRoom[i+move[0]][j+move[1]] in students[classRoom[i][j]]:
          count += 1
    if count == 1:
      result += 1
    elif count == 2:
      result += 10
    elif count == 3:
      result += 100
    elif count == 4:
      result += 1000

print(result)