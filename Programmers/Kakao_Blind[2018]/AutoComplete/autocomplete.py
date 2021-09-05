def compare2(word, target):
  for i in range(len(target)):
    if i == len(target)-1:
      return len(target)
    if word[:i+1] != target[:i+1]:
      return i+1
      
def compare3(word1, target, word2):
  for i in range(len(target)):
    if i == len(target)-1:
      return len(target)
    if word1[:i+1] != target[:i+1] and word2[:i+1] != target[:i+1]:
      return i+1


def solution(words):
  answer = 0
  words.sort()
  for i in range(len(words)):
    if i == 0:
      print(words[i+1], words[i])
      answer += compare2(words[i+1], words[i])
    elif i == len(words)-1:
      print(words[i-1], words[i])
      answer += compare2(words[i-1], words[i])
    else:
      print(words[i-1], words[i], words[i+1])
      answer += compare3(words[i-1], words[i], words[i+1])

  print(answer)
  return answer

solution(["word","war","warrior","world"])