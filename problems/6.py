# https://projecteuler.net/problem=6

from utils import check

def main():
  final = 0
  squares = 0
  sums = 0
  
  for x in range(1, 101):
    squares += x * x
    sums += x


  final = (sums * sums) - squares

  return final

problem = 6
answer = main()

print("https://projecteuler.net/problem=" + str(problem))
check(answer, problem)
