from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int,input().split())) for _ in range(N)]

houses = []
chickens = []
distances = []

for i in range(N):
  for j in range(N):
    if city[i][j] == 1: # 집
      houses.append([i,j])
    elif city[i][j] == 2: # 치킨집
      chickens.append([i,j])

for house in houses:
  chickenDist = []
  for chicken in chickens:
      chickenDist.append(abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))
  distances.append(chickenDist)

chickenNum = []
for i in range(len(chickens)):
  chickenNum.append(i)
chickenComb=list(combinations(chickenNum, M))

cityDist = 9999
for combination in chickenComb:
  # print("살아남은 치킨집 > ", combination)
  newDist = [[] for _ in range(len(houses))]
  for i in range(len(chickens)):
    if i in combination:
      for j in range(len(distances)):
        newDist[j].append(distances[j][i])
  
  newCityDist = 0
  for house in newDist:
    newCityDist += min(house)

  if newCityDist < cityDist:
    cityDist = newCityDist

print(cityDist)