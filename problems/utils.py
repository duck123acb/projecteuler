import os

def check(program_answer, problem):
  base_dir = os.path.dirname(__file__)
  solutions_path = os.path.join(base_dir, "..", "solutions.txt")
  with open(solutions_path, "r") as solutions_file:
    lines = solutions_file.readlines()
  solution_line = lines[problem - 1].strip()
  solution = float(solution_line)

  if solution == program_answer:
    print(f"{program_answer} is correct! ✅")
    return
  
  print(f"{program_answer} is incorrect. ❌")