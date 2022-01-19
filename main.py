file_name=input()
try:
  with open(f"schedule/{file_name}.py", "w") as f:
    f.write("import os; os.remove(__file__)")
except FileNotFoundError:
  import os
  os.mkdir("schedule")
  with open(f"schedule/{file_name}.py", "w") as f:
    f.write("import os; os.remove(__file__)")
