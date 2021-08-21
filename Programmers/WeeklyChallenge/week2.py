import numpy as np

def solution(scores):
  answer = ""
  scores = np.transpose(scores).tolist()
  for i in range(len(scores)):
    if scores[i][i] == max(scores[i]) or scores[i][i] == min(scores[i]):
      if scores[i].count(scores[i][i]) == 1:
        del scores[i][i]
    total = 0
    for j in range(len(scores[i])):
      total += scores[i][j]
    if total/len(scores[i]) < 50:
      answer += "F"
    elif total/len(scores[i]) < 70:
      answer += "D"
    elif total/len(scores[i]) < 80:
      answer += "C"
    elif total/len(scores[i]) < 90:
      answer += "B"
    else:
      answer += "A"
  return answer