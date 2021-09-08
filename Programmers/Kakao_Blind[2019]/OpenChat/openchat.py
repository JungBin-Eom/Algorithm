# [유저 아이디] 사용자가 [닉네임]으로 채팅방에 입장 - "Enter [유저 아이디] [닉네임]" (ex. "Enter uid1234 Muzi")
# [유저 아이디] 사용자가 채팅방에서 퇴장 - "Leave [유저 아이디]" (ex. "Leave uid1234")
# [유저 아이디] 사용자가 닉네임을 [닉네임]으로 변경 - "Change [유저 아이디] [닉네임]" (ex. "Change uid1234 Muzi")

def solution(record):
  answer = []
  names = {}
  for r in record:
    rList = r.split()
    if rList[0] == 'Enter' or rList[0] == 'Change':
      names[rList[1]] = rList[2]
    
  for r in record:
    rList = r.split()
    if rList[0] == 'Enter':
      answer.append(names[rList[1]]+"님이 들어왔습니다.")
    elif rList[0] == 'Leave':
      answer.append(names[rList[1]]+"님이 나갔습니다.")

  print(answer)
  return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

# 8분