# https://projecteuler.net/problem=1

n = 0

def main():
  global n
  for x in range(1000):
    if x % 3 != 0 and x % 5 != 0:
      continue

    n += x

main()
print(n) # √
