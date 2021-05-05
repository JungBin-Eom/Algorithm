def solution(gems):
  pointR = 0
  pointL = 0
  answer = [0, 100000]
  myGem = {gems[pointR]:1}
  gemKind = len(set(gems))

  while pointR < len(gems) and pointL < len(gems):
    if len(myGem) == gemKind:
      if pointR - pointL < answer[1] - answer[0]:
        answer[0] = pointL+1
        answer[1] = pointR+1
      if myGem[gems[pointL]] == 1:
        del(myGem[gems[pointL]])
      else:
        myGem[gems[pointL]] -= 1
      pointL += 1
    else:
      pointR += 1
      if pointR == len(gems):
        break
      if gems[pointR] in myGem.keys():
        myGem[gems[pointR]] += 1
      else:
        myGem[gems[pointR]] = 1  

  #   print()
  #   print(myGem)
  #   print("pointR :", pointR)
  #   print("pointL :", pointL)
  #   print("answer :", answer)

  # print(answer)
  return answer