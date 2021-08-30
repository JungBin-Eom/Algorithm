count = 0

def find(alphaList, nowWord, goal):
  global count
  # print("now:", nowWord, "count:", count)
  count += 1
  if nowWord == goal:
    return True
  if len(nowWord) == 5:
    return False
  else:
    for alphabet in alphaList:
      newWord = nowWord + alphabet
      if find(alphaList, newWord, goal) == True:
        return True

def solution(word):
  global count
  alphaList = ["A", "E", "I", "O", "U"]
  find(alphaList, "", word)
  return count-1

solution("I")