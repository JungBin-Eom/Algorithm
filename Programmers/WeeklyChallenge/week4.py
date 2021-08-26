def solution(table, languages, preference):
  score = {}
  for t in table:
    for lan, pre in zip(languages, preference):
      if lan in t.split():
        score[t.split()[0]] = score.get(t.split()[0], 0) + (6 - t.split().index(lan))*pre
  score = sorted(score.items(), key=(lambda item: [-item[1], item[0]]))
  answer = score[0][0]

  return answer

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
solution(table, languages, preference)

# 18분 30초