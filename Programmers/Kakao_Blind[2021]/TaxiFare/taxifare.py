import heapq

def dijkstra(map, start):
  distances = {node: float('inf') for node in map}
  distances[start] = 0
  queue = []
  heapq.heappush(queue, [distances[start], start])

  while queue:
    current_distance, current_destination = heapq.heappop(queue)

    if distances[current_destination] < current_distance:
      continue
    
    for new_destination, new_distance in map[current_destination].items():
      distance = current_distance + new_distance
      if distance < distances[new_destination]:
        distances[new_destination] = distance
        heapq.heappush(queue, [distance, new_destination])
    
  return distances

def solution(n, s, a, b, fares):
  answer = float('inf')
  map = {}
  for fare in fares:
    if fare[0] not in map.keys():
      map[fare[0]] = {}
    if fare[1] not in map.keys():
      map[fare[1]] = {}
    map[fare[0]][fare[1]] = fare[2]
    map[fare[1]][fare[0]] = fare[2]
  
  # 시작부터 특정 지점까지 요금(합승하는 경우)
  together = dijkstra(map, s)

  # 합승 지점까지 가서 각자 가는 경우
  for i in range(1, n+1):
    if i in together.keys():
      gotoA = dijkstra(map, i).get(a, float('inf'))
      gotoB = dijkstra(map, i).get(b, float('inf'))
      fare = together.get(i) + gotoA + gotoB
      if fare < answer:
        answer = fare
  return answer

solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]])

# 22분