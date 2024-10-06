# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=565&idTask=456

def dectobin(nombre):

    first = 0
    while 2 ** (first + 1) <= nombre:
        first += 1

    res = 0

    for i in range(first, -1, -1):
        if 2**i <= nombre:
            nombre -= 2**i
            res *= 10
            res += 1
        else:
            res *= 10

    return res


cote = int(input())
valeurs = [[a * i for a in range(1, cote + 1)] for i in range(1, cote + 1)]

valeurs = [list(map(dectobin, val)) for val in valeurs]

for ligne in valeurs:
    for valeur in ligne:
        print(valeur, end="\t")
    print()
