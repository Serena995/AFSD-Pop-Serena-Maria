# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
from asyncio import all_tasks

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

print(*progres)

while "_" in progres and incercari_ramase > 0:
    litera = input("Alege o litera: ")
    if "a" <= litera <= "z":
        pass
    else:
        print("Alege doar litere")
        continue

if litera in cuvant_de_ghicit:
    for i in range(len(cuvant_de_ghicit)):
        if cuvant_de_ghicit[i] == litera:
            progres[i] = litera
    print("Ai ghicit o noua litera")
else:
    incercari_ramase -= 1
    print(f"{incercari_ramase} incercari ramase")

all_tasks(loop=all_tasks*len(cuvant_de_ghicit))