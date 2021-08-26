# 09:00부터 n회 t분 간격으로 역에 도착
# 최대 m명 탑승
# 도착한 순간 줄을 선 크루도 탑승
# 셔틀을 타고 사무실로 갈 수 있는 도착시각 중 제일 늦은 시각 구하기
# 대기열 제일 뒤에 섬
# 23:59에는 집으로(다음날 셔틀 타는 일 없음)
def timeToStr(time):
  time = list(map(str, time))
  strTime = ""
  if len(time[0]) == 1:
    strTime += "0"
  strTime += time[0]+":"
  if len(time[1]) == 1:
    strTime += "0"
  strTime += time[1]
  return strTime

def solution(n, t, m, timetable):
  timetable = sorted(timetable)
  answer = ""
  busArrived = "09:00"
  for i in range(n):
    # print("BUS arrived at ", busArrived) 
    busIn = 0
    for crew in timetable:
      if crew <= busArrived:
        busIn += 1
      if busIn == m:
        break
    if i == n-1: # 막차
      if busIn == m:
        answer = timetable[busIn-1]+"-m"
      else:
        answer = busArrived
    timetable = timetable[busIn:]
    busTime = list(map(int, busArrived.split(":")))
    busTime[1] += t
    while busTime[1] >= 60:
      busTime[0] += 1
      busTime[1] -= 60
    busArrived = timeToStr(busTime)

  if answer[-1] == "m":
    answer = answer[:5]
    answer = list(map(int, answer.split(":")))
    answer[1] -= 1
    if answer[1] < 0:
      answer[0] -= 1
      answer[1] = 59
    answer = timeToStr(answer)
  # print(answer)
  return answer

n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]

solution(n, t, m, timetable)

# 42분 32초