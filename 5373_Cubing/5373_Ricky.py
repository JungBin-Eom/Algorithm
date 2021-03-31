import copy

n = int(input())
cubeU = [['w'] * 3 for _ in range(3)] # 위
cubeD = [['y'] * 3 for _ in range(3)] # 아래
cubeF = [['r'] * 3 for _ in range(3)] # 앞
cubeB = [['o'] * 3 for _ in range(3)] # 뒤
cubeL = [['g'] * 3 for _ in range(3)] # 좌
cubeR = [['b'] * 3 for _ in range(3)] # 우
result = []

def clock(cubeSide):
  temp = cubeSide[0][0]
  cubeSide[0][0] = cubeSide[2][0]
  cubeSide[2][0] = cubeSide[2][2]
  cubeSide[2][2] = cubeSide[0][2]
  cubeSide[0][2] = temp
  temp = cubeSide[0][1]
  cubeSide[0][1] = cubeSide[1][0]
  cubeSide[1][0] = cubeSide[2][1]
  cubeSide[2][1] = cubeSide[1][2]
  cubeSide[1][2] = temp
  return cubeSide

def unclock(cubeSide):
  temp = cubeSide[0][0]
  cubeSide[0][0] = cubeSide[0][2]
  cubeSide[0][2] = cubeSide[2][2]
  cubeSide[2][2] = cubeSide[2][0]
  cubeSide[2][0] = temp
  temp = cubeSide[0][1]
  cubeSide[0][1] = cubeSide[1][2]
  cubeSide[1][2] = cubeSide[2][1]
  cubeSide[2][1] = cubeSide[1][0]
  cubeSide[1][0] = temp
  return cubeSide

for i in range (n):
  cubeU = [['w'] * 3 for _ in range(3)] # 위
  cubeD = [['y'] * 3 for _ in range(3)] # 아래
  cubeF = [['r'] * 3 for _ in range(3)] # 앞
  cubeB = [['o'] * 3 for _ in range(3)] # 뒤
  cubeL = [['g'] * 3 for _ in range(3)] # 좌
  cubeR = [['b'] * 3 for _ in range(3)] # 우
  count = int(input())
  rotations = input().split()
  for rotate in rotations:
    side = rotate[0]
    direction = rotate[1]
    if side == 'U':
      if direction == '+':
        cubeU = clock(cubeU)
        temp1, temp2, temp3 = cubeL[0][2], cubeL[1][2], cubeL[2][2]
        cubeL[0][2], cubeL[1][2], cubeL[2][2] = cubeF[0][0], cubeF[0][1], cubeF[0][2]
        cubeF[0][0], cubeF[0][1], cubeF[0][2] = cubeR[2][0], cubeR[1][0], cubeR[0][0]
        cubeR[2][0], cubeR[1][0], cubeR[0][0] = cubeB[2][2], cubeB[2][1], cubeB[2][0]
        cubeB[2][2], cubeB[2][1], cubeB[2][0] = temp1, temp2, temp3
      elif direction == '-':
        cubeU = unclock(cubeU)
        temp1, temp2, temp3 = cubeL[0][2], cubeL[1][2], cubeL[2][2]
        cubeL[0][2], cubeL[1][2], cubeL[2][2] = cubeB[2][2], cubeB[2][1], cubeB[2][0]
        cubeB[2][2], cubeB[2][1], cubeB[2][0] = cubeR[2][0], cubeR[1][0], cubeR[0][0]
        cubeR[2][0], cubeR[1][0], cubeR[0][0] = cubeF[0][0], cubeF[0][1], cubeF[0][2]
        cubeF[0][0], cubeF[0][1], cubeF[0][2] = temp1, temp2, temp3
    elif side == 'D':
      if direction == '+':
        cubeD = clock(cubeD)
        temp1, temp2, temp3 = cubeF[2][0], cubeF[2][1], cubeF[2][2]
        cubeF[2][0], cubeF[2][1], cubeF[2][2] = cubeL[0][0], cubeL[1][0], cubeL[2][0]
        cubeL[0][0], cubeL[1][0], cubeL[2][0] = cubeB[0][2], cubeB[0][1], cubeB[0][0]
        cubeB[0][2], cubeB[0][1], cubeB[0][0] = cubeR[2][2], cubeR[1][2], cubeR[0][2]
        cubeR[2][2], cubeR[1][2], cubeR[0][2] = temp1, temp2, temp3 
      elif direction == '-':
        cubeD = unclock(cubeD)
        temp1, temp2, temp3 = cubeF[2][0], cubeF[2][1], cubeF[2][2]
        cubeF[2][0], cubeF[2][1], cubeF[2][2] = cubeR[2][2], cubeR[1][2], cubeR[0][2]
        cubeR[2][2], cubeR[1][2], cubeR[0][2] = cubeB[0][2], cubeB[0][1], cubeB[0][0]
        cubeB[0][2], cubeB[0][1], cubeB[0][0] = cubeL[0][0], cubeL[1][0], cubeL[2][0]
        cubeL[0][0], cubeL[1][0], cubeL[2][0] = temp1, temp2, temp3
    elif side == 'F':
      if direction == '+':
        cubeF = clock(cubeF)
        temp1, temp2, temp3 = cubeU[2][0], cubeU[2][1], cubeU[2][2]
        cubeU[2][0], cubeU[2][1], cubeU[2][2] = cubeL[2][0], cubeL[2][1], cubeL[2][2]
        cubeL[2][0], cubeL[2][1], cubeL[2][2] = cubeD[0][2], cubeD[0][1], cubeD[0][0]
        cubeD[0][2], cubeD[0][1], cubeD[0][0] = cubeR[2][0], cubeR[2][1], cubeR[2][2]
        cubeR[2][0], cubeR[2][1], cubeR[2][2] = temp1, temp2, temp3
      elif direction == '-':
        cubeF = unclock(cubeF)
        temp1, temp2, temp3 = cubeU[2][0], cubeU[2][1], cubeU[2][2]
        cubeU[2][0], cubeU[2][1], cubeU[2][2] = cubeR[2][0], cubeR[2][1], cubeR[2][2]
        cubeR[2][0], cubeR[2][1], cubeR[2][2] = cubeD[0][2], cubeD[0][1], cubeD[0][0]
        cubeD[0][2], cubeD[0][1], cubeD[0][0] = cubeL[2][0], cubeL[2][1], cubeL[2][2]
        cubeL[2][0], cubeL[2][1], cubeL[2][2] = temp1, temp2, temp3
    elif side == 'B':
      if direction == '+':
        cubeB = clock(cubeB)
        temp1, temp2, temp3 = cubeD[2][0], cubeD[2][1], cubeD[2][2]
        cubeD[2][0], cubeD[2][1], cubeD[2][2] = cubeL[0][2], cubeL[0][1], cubeL[0][0]
        cubeL[0][2], cubeL[0][1], cubeL[0][0] = cubeU[0][2], cubeU[0][1], cubeU[0][0]
        cubeU[0][2], cubeU[0][1], cubeU[0][0] = cubeR[0][2], cubeR[0][1], cubeR[0][0]
        cubeR[0][2], cubeR[0][1], cubeR[0][0] = temp1, temp2, temp3
      elif direction == '-':
        cubeB = unclock(cubeB)
        temp1, temp2, temp3 = cubeR[0][2], cubeR[0][1], cubeR[0][0]
        cubeR[0][2], cubeR[0][1], cubeR[0][0] = cubeU[0][2], cubeU[0][1], cubeU[0][0]
        cubeU[0][2], cubeU[0][1], cubeU[0][0] = cubeL[0][2], cubeL[0][1], cubeL[0][0]
        cubeL[0][2], cubeL[0][1], cubeL[0][0] = cubeD[2][0], cubeD[2][1], cubeD[2][2]
        cubeD[2][0], cubeD[2][1], cubeD[2][2] = temp1, temp2, temp3
    elif side == 'L':
      if direction == '+':
        cubeL = clock(cubeL)
        temp1, temp2, temp3 = cubeB[0][0], cubeB[1][0], cubeB[2][0]
        cubeB[0][0], cubeB[1][0], cubeB[2][0] = cubeD[0][0], cubeD[1][0], cubeD[2][0]
        cubeD[0][0], cubeD[1][0], cubeD[2][0] = cubeF[0][0], cubeF[1][0], cubeF[2][0]
        cubeF[0][0], cubeF[1][0], cubeF[2][0] = cubeU[0][0], cubeU[1][0], cubeU[2][0]
        cubeU[0][0], cubeU[1][0], cubeU[2][0] = temp1, temp2, temp3
      elif direction == '-':
        cubeL = unclock(cubeL)
        temp1, temp2, temp3 = cubeB[0][0], cubeB[1][0], cubeB[2][0]
        cubeB[0][0], cubeB[1][0], cubeB[2][0] = cubeU[0][0], cubeU[1][0], cubeU[2][0]
        cubeU[0][0], cubeU[1][0], cubeU[2][0] = cubeF[0][0], cubeF[1][0], cubeF[2][0]
        cubeF[0][0], cubeF[1][0], cubeF[2][0] = cubeD[0][0], cubeD[1][0], cubeD[2][0]
        cubeD[0][0], cubeD[1][0], cubeD[2][0] = temp1, temp2, temp3
    elif side == 'R':
      if direction == '+':
        cubeR = clock(cubeR)
        temp1, temp2, temp3 = cubeB[2][2], cubeB[1][2], cubeB[0][2]
        cubeB[2][2], cubeB[1][2], cubeB[0][2] = cubeU[2][2], cubeU[1][2], cubeU[0][2]
        cubeU[2][2], cubeU[1][2], cubeU[0][2] = cubeF[2][2], cubeF[1][2], cubeF[0][2]
        cubeF[2][2], cubeF[1][2], cubeF[0][2] = cubeD[2][2], cubeD[1][2], cubeD[0][2]
        cubeD[2][2], cubeD[1][2], cubeD[0][2] = temp1, temp2, temp3
      elif direction == '-':
        cubeR = unclock(cubeR)
        temp1, temp2, temp3 = cubeB[2][2], cubeB[1][2], cubeB[0][2]
        cubeB[2][2], cubeB[1][2], cubeB[0][2] = cubeD[2][2], cubeD[1][2], cubeD[0][2]
        cubeD[2][2], cubeD[1][2], cubeD[0][2] = cubeF[2][2], cubeF[1][2], cubeF[0][2]
        cubeF[2][2], cubeF[1][2], cubeF[0][2] = cubeU[2][2], cubeU[1][2], cubeU[0][2]
        cubeU[2][2], cubeU[1][2], cubeU[0][2] = temp1, temp2, temp3
    # print("U:", cubeU)
    # print("L:", cubeL)
    # print("B:", cubeB)
    # print("R:", cubeR)
    # print("F:", cubeF)
    # print("D:", cubeD)
    # print()

  result.append(cubeU)

for case in result:
  for line in case:
    print(line[0]+line[1]+line[2])