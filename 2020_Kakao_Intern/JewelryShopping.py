def solution(gems):
  pointR = 0
  pointL = 0
  answer = [0, 100000]
  gemKind = len(list(set(gems)))
  myGem = {}
  for gem in gems:
    myGem[gem] = 0

  while pointR != len(gems) and pointL != len(gems) and pointR >= pointL:
    if 0 in myGem.values():
      myGem[gems[pointR]] += 1
      pointR += 1
    if 0 not in myGem.values():
      if pointR - pointL < answer[1] - answer[0]:
        answer[0] = pointL+1
        answer[1] = pointR
      if pointR - pointL + 1 == gemKind:
        break
      myGem[gems[pointL]] -= 1
      pointL += 1

  #   print()
  #   print(myGem)
  #   print("pointR :", pointR)
  #   print("pointL :", pointL)
  #   print("answer :", answer)

  # print(answer)
  return answer

# solution([["XYZ", "XYZ", "XYZ"])