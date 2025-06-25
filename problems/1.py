# https://projecteuler.net/problem=1

from utils import check

def main():
  final = 0

  for x in range(1000):
    if x % 3 != 0 and x % 5 != 0:
      continue

    final += x

  return final

problem = 1
answer = main()

print("https://projecteuler.net/problem=" + str(problem))
check(answer, problem)
