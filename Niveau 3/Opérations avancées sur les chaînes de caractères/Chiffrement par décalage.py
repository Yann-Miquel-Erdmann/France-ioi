# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=556&idTask=2426

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


for i in range(2, int(input()) + 1):
    texte = input()
    decalage = 3 * i if i % 2 == 0 else -5 * i
    decalage = decalage % 26
    decrypte = []
    for lettre in texte:
        if lettre.islower():
            index = alphmin.index(lettre) - decalage + 1
            decrypte.append(alphmin[(index if index > 0 else index + 26) - 1])

        elif lettre.isupper():
            index = alphmax.index(lettre) - decalage + 1
            decrypte.append(alphmax[(index if index > 0 else index + 26) - 1])

        else:
            decrypte.append(lettre)

    print("".join(decrypte))
