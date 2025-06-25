# https://projecteuler.net/problem=2

problem = 2
final = 0

def check():
  pass

def main():
  global final
  
  n1 = 1
  n2 = 1

  while n2 <= 4e6:
    n1, n2 = n2, n1 + n2

    if not n2 % 2 == 0:
      continue

    final += n2

main()
print(final) # 4613732
