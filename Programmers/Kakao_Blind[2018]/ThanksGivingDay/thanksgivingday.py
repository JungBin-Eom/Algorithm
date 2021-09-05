# 초당 최대 처리량 = 임의 시간부터 1초간 처리하는 요청의 최대 개수
# 응답 완료 시간: 2016-09-15 hh:mm:ss.sss
# 처리 시간: s로 끝남(3초 이하)
# lines는 응답 완료 시간을 기준으로 정렬\

def solution(lines):
  answer = 0

  times = []
  for line in lines:
    time = line[11:]
    hour = int(time[:2])
    minute = int(time[3:5])
    second = int(time[6:8])
    milli = int(time[9:12])
    t = int(float(time[13:len(time)-1])*1000)
    end = (3600*hour + 60*minute + second)*1000 + milli
    start = (end - t) + 1
    times.append((start, end))

  for i in range(len(times)):
    # frontCount1 = 0
    # for j in range(len(times)):
    #   if times[i][0]-1 < times[j][0] <= times[i][0] or times[i][0]-1 < times[j][1] <= times[i][0]:
    #     frontCount1 += 1
    #   elif j > i and times[j][0] < times[i][0] and times[j][1] > times[i][1]:
    #     frontCount1 += 1

    # frontCount2 = 0
    # for j in range(len(times)):
    #   if times[i][0] <= times[j][0] < times[i][0]+1 or times[i][0] <= times[j][1] < times[i][0]+1:
    #     frontCount2 += 1
    #   elif j > i and times[j][0] < times[i][0] and times[j][1] > times[i][1]:
    #     frontCount2 += 1
    
    # backCount1 = 0
    # for j in range(len(times)):
    #   if times[i][1]-1 < times[j][0] <= times[i][1] or times[i][1]-1 < times[j][1] <= times[i][1]:
    #     backCount1 += 1
    #   elif j > i and times[j][0] < times[i][0] and times[j][1] > times[i][1]:
    #     backCount1 += 1
    
    # backCount2 = 0
    # for j in range(len(times)):
    #   if times[i][1] <= times[j][0] < times[i][1]+1 or times[i][1] <= times[j][1] < times[i][1]+1:
    #     backCount2 += 1
    #   elif j > i and times[j][0] < times[i][0] and times[j][1] > times[i][1]:
    #     backCount2 += 1
    count = 0
    for j in range(i, len(times)):
      if times[i][1] > times[j][0] - 1000:
        count += 1
    answer = max(answer, count)
    # if answer < max(frontCount1, frontCount2, backCount1, backCount2):
    #   answer = max(frontCount1, frontCount2, backCount1, backCount2)

  print(answer)
  return answer

# 2시간 22분