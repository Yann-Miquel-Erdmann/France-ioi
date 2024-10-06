# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=556&idTask=468

chiffrement = list(input())

dico = {}
for a, i in zip(
    chiffrement,
    [
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
    ],
):
    dico[i] = a


message = input()
decrypte = []
for lettre in message:
    if lettre.isalpha():
        if lettre.isupper():
            decrypte.append(dico[lettre.lower()].upper())
        else:
            decrypte.append(dico[lettre])
    else:
        decrypte.append(lettre)

print("".join(decrypte))
