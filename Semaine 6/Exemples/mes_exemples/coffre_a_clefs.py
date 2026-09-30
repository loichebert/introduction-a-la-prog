import math
h = 0
for i in range(600, 700, 2):
    i = str(i)
    if "3" in i:
        if sum(int(c) for c in list(i)) == 11:
            print(f"{i} est la bonne réponse")
            break
