def solution(numbers, hand):
  answer = ""
  nowL = [3,0]
  nowR = [3,2]

  for number in numbers:
    if number == 1 or number == 4 or number == 7:
      answer += "L"
      nowL = [number//3, 0]
    elif number == 3 or number == 6 or number == 9:
      answer += "R"
      nowR = [number//3 - 1, 2]
    else:
      if number == 0:
        numberX = 3
      else:
        numberX = number//3
      numberY = 1
      LeftDistance  = abs(nowL[0] - numberX) + abs(nowL[1] - numberY)
      RightDistance = abs(nowR[0] - numberX) + abs(nowR[1] - numberY)

      if LeftDistance < RightDistance:
        answer += "L"
        nowL = [numberX, 1]
      elif RightDistance < LeftDistance:
        answer += "R"
        nowR = [numberX, 1]
      else:
        if hand == "left":
          answer += "L"
          nowL = [numberX, 1]
        else:
          answer += "R"
          nowR = [numberX, 1]

  return answer