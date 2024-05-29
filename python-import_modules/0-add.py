#!/usr/bin/python3
with open("add_0.py", "r") as file:
    code = file.read()

exec(code)

resultat = add(1, 2)

print(f"1 + 2 =", resultat)
