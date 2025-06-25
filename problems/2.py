# https://projecteuler.net/problem=2

from utils import check

def main():
  final = 0
  
  n1 = 1
  n2 = 1

  while n2 <= 4e6:
    n1, n2 = n2, n1 + n2

    if not n2 % 2 == 0:
      continue

    final += n2

  return final


problem = 2
answer = main()

print(f"https://projecteuler.net/problem={problem}")
check(answer, problem)
