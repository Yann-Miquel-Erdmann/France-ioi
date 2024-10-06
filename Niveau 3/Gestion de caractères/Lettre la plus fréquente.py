# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=566&idTask=467

alph = [
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

frequence = [0] * 26

for lettre in [char for char in input().upper() if char != " "]:
    frequence[alph.index(lettre)] += 1
print(alph[frequence.index(max(frequence))])
