# https://projecteuler.net/problem=4

from utils import check

def is_palindrome(number):
  s = str(number)
  return s == s[::-1]


def main():
  final = 0

  for n1 in range(900, 1000):
    for n2 in range(900, 1000):
      product = n1 * n2
      if not is_palindrome(product):
        continue
      
      if product > final: # kinda redundant here but just for good practice
        final = product



  return final

problem = 4
answer = main()

print("https://projecteuler.net/problem=" + str(problem))
check(answer, problem)
