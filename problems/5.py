# https://projecteuler.net/problem=5

from utils import check

def is_divisible(n):
  for m in range(11, 21):
    if n % m == 0:
      continue
    
    return False
  
  return True


def main():
  final = 2520

  while not is_divisible(final):
    final += 20

  return final

problem = 5
answer = main()

print("https://projecteuler.net/problem=" + str(problem))
check(answer, problem)
