# https://projecteuler.net/problem=9

import math
from utils import check

def main():
  final = 0
  
  for i in range(1, 1000):
    for j in range(1, 1000):
      k = math.sqrt((i * i) + (j * j))
      if k.is_integer() and (i + j + k) == 1000:
        final = i * k * j
        break

  return final

problem = 9
answer = main()

print("https://projecteuler.net/problem=" + str(problem))
check(answer, problem)
