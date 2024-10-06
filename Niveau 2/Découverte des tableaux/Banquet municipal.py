# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=651&idTask=2080

positions = []
longueur = int(input())
changements = int(input())
for i in range(longueur):
    positions.append(int(input()))
for i in range(changements):
    pos1 = int(input())
    pos2 = int(input())
    temp = positions[pos1]
    positions[pos1] = positions[pos2]
    positions[pos2] = temp


for pos in positions:
    print(pos)
