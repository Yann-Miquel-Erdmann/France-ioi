# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=761&idTask=907

alphamaj = [
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
mot = ""
for _ in range(int(input())):
    for i, char in enumerate(list(input())):
        if char == "O":
            mot += alphamaj[i]

print(mot)
