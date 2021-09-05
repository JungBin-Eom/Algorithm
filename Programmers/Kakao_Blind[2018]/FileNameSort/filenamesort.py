numbers = '0123456789'

def solution(files):
  answer = []
  fileInfoList = []
  for file in files:
    index = files.index(file)
    head = ''
    number = 0
    tail = ''
    for i in range(len(file)):
      if file[i] in numbers:
        head = file[:i].lower()
        j = i
        while j < len(file):
          if file[j] in numbers:
            j += 1
          else:
            break
        number = int(file[i:j])
        tail = file[j:]
        break
    fileInfoList.append((head, number, tail, index))
    
  fileInfoList = sorted(fileInfoList, key=lambda file:(file[0], file[1]))
  print(fileInfoList)

  for fileInfo in fileInfoList:
    answer.append(files[fileInfo[3]])
  print(answer)
  return answer

solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])

# 18분