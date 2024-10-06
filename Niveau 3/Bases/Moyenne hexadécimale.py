# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=565&idTask=457

def basetodec(base, valeurs):
    resultat = 0
    for i, bit in enumerate(valeurs[::-1]):
        resultat += int(bit) * base**i
    return resultat


def dectobase(base, nombre):
    first = 0
    while base ** (first + 1) <= nombre:
        first += 1

    valeurs = []
    for i in range(first, -1, -1):
        if base**i <= nombre:
            fois = nombre // base**i
            nombre = nombre % base**i
            valeurs.append(fois)
        else:
            valeurs.append(0)

    return valeurs


hexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

vals = []
for char in input():
    vals.append(hexa.index(char))


it = basetodec(16, vals)
values = []
for i in range(it):
    vals = []
    for char in input():
        vals.append(hexa.index(char))
    values.append(basetodec(16, vals))


moy = int(sum(values) / len(values))
print("".join(map(lambda x: hexa[int(x)], dectobase(16, moy))))
