# https://projecteuler.net/problem=7

from utils import check

def is_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(3, int(n**0.5) + 1, 2): # start at 3 | check until the square root of the number because if by then there are no factors, there will never be any factors | increment by 2 
    if n % i == 0:
      return False
  return True

def main():
  final = 3
  amt_prime = 2
  
  
  while amt_prime < 10001:
    final += 2
    if is_prime(final):
      amt_prime += 1

  return final

problem = 7
answer = main()

print("https://projecteuler.net/problem=" + str(problem))
check(answer, problem)
