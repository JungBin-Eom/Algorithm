def solution(n, t, m, p):
  answer = ''
  number = 1
  numStr = '0'
  maxNumLen = t*m
  while len(numStr) < maxNumLen:
    notation = ''
    mynum = number
    while mynum > 0:
      mod = mynum % n
      mynum = mynum // n
      if mod >= 10:
        mod = chr(mod+55)
      notation = str(mod) + notation
    numStr += notation
    number += 1
  
  while len(answer) != t:
    answer += numStr[p-1]
    numStr = numStr[m:]
  
  return answer

solution(16, 16, 2, 1)

# 31분