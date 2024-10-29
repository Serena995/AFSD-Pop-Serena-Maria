meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

while studenti:
    student=studenti.pop(0)
    comanda=comenzi.pop(0)
    tavi=list(tavi).pop()
    istoric_comenzi.append(comanda)
    print(f'{student} a comandat {comanda}')

print(istoric_comenzi)
numar_ceafa=istoric_comenzi.count('ceafa')
numar_papanasi=istoric_comenzi.count('papanasi')
numar_guias=istoric_comenzi.count('guias')
print(f'S-au comandat {numar_ceafa} cefe, {numar_papanasi} papanasi, {numar_guias} guias')

numar_tavi=len(tavi)
print(f'Mai sunt {numar_tavi} tavi')

print('Mai este ceafa:')
for numar_ceafa in istoric_comenzi:
    if numar_ceafa < str(3):
        print(f'True')
    else:
        print(f'False')

print('Mai sunt papanasi:')
for numar_papanasi in istoric_comenzi:
    if numar_papanasi < str(10):
        print(f'True')
    else:
        print(f'False')

print('Mai este guias:')
for numar_guias in istoric_comenzi:
    if numar_guias < str(6) :
        print(f'True')
    else:
        print(f'False')

print('Cantina a incasat:')
pret_papanasi = numar_papanasi.count('papanasi') * int(preturi[0][1])
pret_ceafa = numar_ceafa.count('ceafa') * int(preturi[1][1])
pret_guias = numar_guias.count('guias') * int(preturi[2][1])
profit = (pret_papanasi + pret_ceafa + pret_guias)
print(f'{profit} lei')

print('Produse care costa cel mult 7 lei:')
produs_ieftin=[]
for mancare_pret in preturi:
    pret_mancare = mancare_pret[1]
    nume_mancare = mancare_pret[0]
    if pret_mancare <= 7:
        produs_ieftin.append(nume_mancare)
print(produs_ieftin)
