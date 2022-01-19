file_name=input()

with open(f"schedule/{file_name}.py", "w") as f:
  f.write("import os; os.remove(__file__)")
