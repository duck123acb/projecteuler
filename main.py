import os

problem = input("What problem are you gonna solve?\n")
print(f"Creating problems/{problem}.py ...")

file_contents = f'''# https://projecteuler.net/problem={problem}

from utils import check

def main():
  final = 0
  
  # solve here ig

  return final

problem = {problem}
answer = main()

print("https://projecteuler.net/problem=" + str(problem))
check(answer, problem)
'''

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "problems/", f"{problem}.py")
with open(path, "x") as new_file:
  new_file.write(file_contents)

print(f"problems/{problem}.py created!")
