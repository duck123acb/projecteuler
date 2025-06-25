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

  for x in range(1000):
    if x % 3 != 0 and x % 5 != 0:
      continue

    final += x

  return final

problem = 1
answer = main()

print("https://projecteuler.net/problem=" + str(problem))
check(answer)
