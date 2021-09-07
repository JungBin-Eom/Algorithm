def solution(play_time, adv_time, logs):
  hour = int(play_time[:2])
  minute = int(play_time[3:5])
  second = int(play_time[6:8])
  playEnd = 3600*hour + 60*minute + second

  viewers = [0 for _ in range(playEnd+1)]

  hour = int(adv_time[:2])
  minute = int(adv_time[3:5])
  second = int(adv_time[6:8])
  adv = 3600*hour + 60*minute + second

  for log in logs:
    hour = int(log[:2])
    minute = int(log[3:5])
    second = int(log[6:8])
    start = 3600*hour + 60*minute + second

    hour = int(log[9:11])
    minute = int(log[12:14])
    second = int(log[15:17])
    end = 3600*hour + 60*minute + second

    viewers[start] += 1
    viewers[end] -= 1

  for i in range(1, playEnd):
    viewers[i] = viewers[i-1] + viewers[i]

  for i in range(1, playEnd):
    viewers[i] = viewers[i-1] + viewers[i]
    
  maxViewer = 0
  answer = 0
  for i in range(adv-1, playEnd):
    if i >= adv:
      if viewers[i]-viewers[i-adv] > maxViewer:
        maxViewer = viewers[i]-viewers[i-adv]
        answer = i-adv+1
    else:
      if maxViewer < viewers[i]:
        maxViewer = viewers[i]
        answer = i-adv+1
    
  hour = answer // 3600
  answer -= 3600*hour
  minute = answer // 60
  answer -= 60*minute

  hour = "0"+str(hour) if hour < 10 else str(hour)
  minute = "0"+str(minute) if minute < 10 else str(minute)
  second = "0"+str(answer) if answer < 10 else str(answer)

  answer = hour+":"+minute+":"+second

  print(answer)
  return answer

solution(	"99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])

# 2시간 1분
# 체감 난이도 상상상
# 시간 -> 초단위로 바꾸는거 ok
# 누적 시청자를 list로 처리하는게 생각해내기 어려웠음
# i때 시청자 - i-adv때 시청자 = i - adv + 1부터 i까지 광고 나올 때 시청자 수
# 광고 시간을 기준으로 시청자 수를 찾아야 하므로 광고가 끝나는 시간 -> 광고가 시작하는 시간 순으로 찾기