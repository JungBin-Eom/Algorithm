from itertools import combinations

def solution(orders, course):
  answer = []
  for num in course:
    menus = {}
    for order in orders:
      menuComb = []
      if len(order) >= num:
        menuComb = list(combinations(order, num))
        # print(menuComb)
        print(menuComb)
      for comb in menuComb:
        name = "".join(sorted(comb))
        
        if name in menus.keys():
          menus[name] += 1
        else:
          menus[name] = 1
    print(menus)
    if len(list(menus.values())) != 0:
      maxOrder = max(list(menus.values()))
      if maxOrder > 1:
        for menu in list(menus.keys()):
          if menus[menu] == maxOrder:
            answer.append(menu)

  answer.sort()
  print(answer)
  return answer

solution(["XYZ", "XWY", "WXA"], [2, 3, 4])

# 39분
# counter도 사용해보자