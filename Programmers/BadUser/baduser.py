from itertools import product

def solution(user_id, banned_id):
  banned_users = []
  for banned in banned_id:
    find = []
    for user in user_id:
      if len(user) == len(banned):
        flag = True
        for i in range(len(user)):
          if user[i] != banned[i] and banned[i] != "*":
            flag = False
            break
        if flag == True:
          find.append(user)
    banned_users.append(find)

  banned_users = [list(set(x)) for x in banned_users]
  comb = list(product(*banned_users))
  
  result = set()
  for items in comb:
    items = list(items)
    if len(set(items)) == len(banned_id):
      result.add(tuple(sorted(items)))

  return len(result)


user = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned = ["fr*d*", "*rodo", "******", "******"]
solution(user, banned)