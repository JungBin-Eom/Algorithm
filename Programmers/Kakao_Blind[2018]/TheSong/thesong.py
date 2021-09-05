def solution(m, musicinfos):
  answerList = []
  for musicinfo in musicinfos:
    info = musicinfo.split(",")
    start = int(info[0][:2])*60 + int(info[0][3:])
    end = int(info[1][:2])*60 + int(info[1][3:])
    name = info[2]
    melody = info[3]

    playTime = end - start
    play = ''
    j = 0
    for _ in range(playTime):
      if j < len(melody)-1 and melody[j+1] == '#':
        play += melody[j:j+2]
        j += 1
      else:
        play += melody[j]
      j += 1
      if j == len(melody):
        j = 0

    a = -1
    while play[a+1:].find(m) != -1:
      a = play[a+1:].find(m) + a + 1
      if a+len(m) < len(play):
        if play[a+len(m)] != '#':
          answerList.append((name, playTime))
      else:
        answerList.append((name, playTime))

  answer = ''
  if len(answerList) == 0:
    answer = '(None)'
  elif len(answerList) == 1:
    answer = answerList[0][0]
  else:
    answerList = sorted(answerList, key=lambda song: -song[1])
    answer = answerList[0][0]
  print(answer)
  return answer

solution("CCB",["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"])

# 1시간 1분
# #처리하는게 까다로웠음
# 기억해야 할 것: lambda 사용법, find 사용법, 시간 초로 바꾸기