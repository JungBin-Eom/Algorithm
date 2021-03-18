# input
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

rowCount = 3
colCount = 3
time = 0

def arraySort(maxRowItemCount):
  for row in A:
    sortRow = {}
    newRow = []
 
    for item in row:
      if item != 0:
        if item in sortRow:
          sortRow[item] += 1
        else:
          sortRow[item] = 1

    sortRow = sorted(sortRow.items())
    sortRow = sorted(sortRow, key=lambda x: x[1])
    for key, value in sortRow:
      if len(newRow) <= 100:
        newRow.append(key)
      else:
        break
      if len(newRow) <= 100:
        newRow.append(value)
      else:
        break
      
    if maxRowItemCount < len(newRow):
      maxRowItemCount = len(newRow)
    newA.append(newRow)
  return newA, maxRowItemCount

def transpose(myArray):
  newArray = [[] for _ in range(len(myArray[0]))]
  for row in myArray:
    for i in range(len(row)):
      newArray[i].append(row[i])
  return newArray
    
      
while(time <= 100):
  if rowCount >= r and colCount >= c:
    if A[r-1][c-1] == k:
      break
  
  newA = []
  maxRowItemCount = 0

  if rowCount >= colCount: # R연산
    newA, maxRowItemCount = arraySort(maxRowItemCount)
    for row in newA:
      while len(row) != maxRowItemCount:
        row.append(0)
    A = newA[:]
    colCount = maxRowItemCount

  else: # C연산
    A = transpose(A)
    newA, maxRowItemCount = arraySort(maxRowItemCount)
    for row in newA:
      while len(row) != maxRowItemCount:
        row.append(0)
    A = transpose(newA)
    rowCount = maxRowItemCount
  time += 1

if time > 100:
  print(-1)
else:
  print(time)