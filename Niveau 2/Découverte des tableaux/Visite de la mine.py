# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=651&idTask=2075

deplacements = []

table = {1: 2, 2: 1, 3: 3, 4: 5, 5: 4}

for i in range(int(input())):
    deplacements.append(int(input()))


for deplacement in deplacements[::-1]:
    print(table[deplacement])
