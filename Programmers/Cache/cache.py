def solution(cacheSize, cities):
  answer = 0
  cache = []
  for city in cities:
    city = city.lower()
    if city in cache and cacheSize != 0:
      answer += 1
      cache.remove(city)
      cache.append(city)
    else:
      answer += 5
      if len(cache) == cacheSize:
        cache = cache[1:]
      cache.append(city)
  print(answer)
  
  return answer
  
solution(0, 	["LA", "LA"])
