def solution(msg):
  answer = []
  lzw = {}
  for i in range(1,27):
    lzw[chr(64+i)] = i
    
  while len(msg) != 0:
    inValues = ''
    k = 1
    while k <= len(msg):
      now = msg[:k]
      print(now)
      if now in lzw.keys():
        inValues = now
        k += 1
      else:
        lzw[now] = len(lzw)+1
        break
    msg = msg[k-1:]
    answer.append(lzw[inValues])

  print(answer)
  return answer

solution("KAKAO")

# 14분