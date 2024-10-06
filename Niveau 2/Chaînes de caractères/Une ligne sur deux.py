# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=595&idTask=2403

lignes = []

for i in range(int(input())):
    lignes.append(input())

for i in range(len(lignes)):
    if (i + 1) % 2 == 1:
        print(lignes[i])
