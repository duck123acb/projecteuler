# https://projecteuler.net/problem=3

from utils import check

def main():
  n = 600851475143
  final = 2
  
  while n % 2 == 0: # getting rid of the 2's
    n //= 2 # //= rounds it to an int instead of floating point

  i = 3
  while i * i <= n:  # only check up to the square root of n, since the larger pair would have already been found earlier since the square is the halfway point of factors
    while n % i == 0:  # while i divides n evenly, it's a prime factor. divide n by i to remove that factor. Since all composite numbers are made of smaller prime factors, their factors will have already been removed.
      final = i
      n //= i
    i += 2 # skip even numbers

  if n > 2: # if n is STILL not divisible by anything its prime
    final = n

  return final

problem = 3
answer = main()

print("https://projecteuler.net/problem=" + str(problem))
check(answer, problem)
