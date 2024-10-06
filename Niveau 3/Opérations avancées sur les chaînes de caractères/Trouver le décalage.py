# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=556&idTask=2427

alphmin = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


alphmax = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

frequences = [0] * 26
texte = input()
lettres = [lettre for lettre in texte.lower() if lettre.isalpha()]
for lettre in lettres:
    frequences[alphmin.index(lettre)] += 1

decalage = frequences.index(max(frequences)) - 5

decrypte = []
for lettre in texte:
    if lettre.islower():
        index = alphmin.index(lettre) - decalage
        decrypte.append(alphmin[(index if index > 0 else index + 26) - 1])

    elif lettre.isupper():
        index = alphmax.index(lettre) - decalage
        decrypte.append(alphmax[(index if index > 0 else index + 26) - 1])

    else:
        decrypte.append(lettre)

print("".join(decrypte))
