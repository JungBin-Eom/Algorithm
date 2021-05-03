from itertools import permutations

def solution(expression):
  point = 0
  answer = 0
  polynomial = []
  poly = list(expression)

  for i in range(len(poly)):
    if poly[i] == '+' or poly[i] == '-' or poly[i] == '*':
      polynomial.append(''.join(poly[point:i]))
      polynomial.append(poly[i])
      point = i+1
    elif i == len(poly)-1:
      polynomial.append(''.join(poly[point:i+1]))

  orders = list(permutations(['+','-','*'], 3))
  for order in orders:
    myPoly = polynomial[:]
    
    for oper in order:
      index = 0
      while index < len(myPoly):
        if myPoly[index] == oper:
          myPoly = myPoly[:index-1] + list(str(eval(myPoly[index-1]+oper+myPoly[index+1])).split()) + myPoly[index+2:]
        else:
          index += 1
    
    result = abs(int(myPoly[0]))
    if result > answer:
      answer = result

  return answer

# expression = input()
# solution(expression)