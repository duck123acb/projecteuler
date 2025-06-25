import os

def check(program_answer):
  base_dir = os.path.dirname(__file__)
  solutions_path = os.path.join(base_dir, "..", "solutions.txt")
  with open(solutions_path, "r") as solutions_file:
    lines = solutions_file.readlines()
  solution_line = lines[problem - 1].strip()
  solution = float(solution_line)

  if solution == program_answer:
    print(str(program_answer) + " is correct! ✅")
    return
  
  print(str(program_answer) + " is incorrect. ❌")

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

print("https://projecteuler.net/problem=" + str(problem))
check(answer)
