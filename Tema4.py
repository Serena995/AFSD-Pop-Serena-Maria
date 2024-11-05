# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

print(*progres)

while "_" in progres and incercari_ramase > 0:
    litera=input("Alege o litera: ")
    if len(litera) != 1:
        print("Alege o singura litera")
    elif not litera.isalpha():
        print("Alege doar litere")
        continue
    elif litera in cuvant_de_ghicit:
        for i in  range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
               progres[i] = litera
               print("Ai ghicit o noua litera")
               print("Progresul cuvantului", " ".join(progres))
               print(f"{incercari_ramase} incercari ramase")
               if litera in litere_incercate:
                   print("Alegeti alta litera")
               else:
                   litere_incercate.append(litera)
                   print("Litere incercate:", " ".join(litere_incercate))
    else:
        incercari_ramase -= 1
        print(f"Incorect. {incercari_ramase} incercari ramase")
        print("Progresul cuvantului", " ".join(progres))
        if litera in litere_incercate:
            print("Alegeti alta litera")
        else:
            litere_incercate.append(litera)
            print("Litere incercate:", " ".join(litere_incercate))

if "_" not in progres and incercari_ramase != 0:
    print("Felicitări! Ai ghicit cuvântul!")
else:
    print("Ai pierdut! Cuvântul era: ", {cuvant_de_ghicit})


