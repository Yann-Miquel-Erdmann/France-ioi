# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=566&idTask=2419

alph = [
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


frequences = [0] * 26

lettres = [lettre for lettre in input().lower() if lettre.isalpha()]
for lettre in lettres:
    frequences[alph.index(lettre)] += 1


for frequence in frequences:
    print(frequence / len(lettres))
