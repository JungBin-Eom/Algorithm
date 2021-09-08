from bisect import bisect_left, bisect_right

fills = [[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,0,0],[1,0,1,0],[1,0,0,1],[0,1,1,0],[0,1,0,1],[0,0,1,1],[1,1,1,0],[1,1,0,1],[1,0,1,1],[0,1,1,1],[1,1,1,1]]

def solution(info, query):
  answer = []

  infos = {}
  for applicant in info:
    infoList = applicant.split()
    score = int(infoList[-1])
    applicantInfo = infoList[:-1]

    for fill in fills:
      infoStr = ''
      for i in range(4):
        if fill[i] == 0:
          infoStr += '-'
        else:
          infoStr += applicantInfo[i]
      # print(infoStr)
      if infoStr not in infos.keys():
        infos[infoStr] = []
      infos[infoStr].append(score)

  for value in infos.values():
    value.sort()

  for condition in query:
    condList = condition.split()
    condList = list(filter(lambda x: x!='and', condList))
    condScore = int(condList[-1])
    condStr = ''.join(condList[:-1])
    if condStr in infos:
      data = infos[condStr]
      if len(data) > 0:
        l = 0
        r = len(data)
        while l != r and l != len(data):
          if data[(l+r) // 2] >= condScore:
            r = (l+r)//2
          else:
            l = (l+r)//2 + 1
      answer.append(len(data)-l)
    else:
      answer.append(0)
        
  return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])

# 1시간 13분
# -를 처리하는 방법 -> info가 주어졌을 때 -를 문자열에 포함하여 key로 사용하는 방법을 알아내기 힘들었음
# filter함수: list에서 원하는 조건에 맞는 값들만 걸러내는 함수
# binary search: l과 r을 주어주고 condScore에 해당하는 경계값을 찾는 과정이 어려웠음
# 처음에는 모두 하나씩 탐색했지만 역시나 시간오버->binary search로 반반 탐색