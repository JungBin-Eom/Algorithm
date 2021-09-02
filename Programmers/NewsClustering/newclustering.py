# J(A,B)는 교집합의 크기를 합집합의 크기로 나눈 값

import math

def intersection(list1, list2):
  result = list1[:]
  list1Copy = list1[:]
  for item in list2:
    if item not in list1Copy:
      result.append(item)
    else:
      list1Copy.remove(item)
  return result

def union(list1, list2):
  result = []
  list1Copy = list1[:]
  for item in list2:
    if item in list1Copy:
      list1Copy.remove(item)
      result.append(item)

  return result

def solution(str1, str2):
  answer = 0
  str1List = []
  str2List = []

  for i in range(len(str1)-1):
    if str1[i].isalpha() and str1[i+1].isalpha():
      str1List.append((str1[i]+str1[i+1]).lower())
  
  for i in range(len(str2)-1):
    if str2[i].isalpha() and str2[i+1].isalpha():
      str2List.append((str2[i]+str2[i+1]).lower())
      
  
  inter = intersection(str1List, str2List)
  uni = union(str1List, str2List)

  if len(inter) == 0:
    answer = 1
  else:
    answer = len(uni) / len(inter)
  answer *= 65536
  answer = math.trunc(answer)
  # print(answer)
  return answer

solution("aa1+aa2", "AAAA12")

# 38분