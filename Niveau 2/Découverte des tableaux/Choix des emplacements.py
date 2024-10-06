# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=651&idTask=2081

marchands = []

for i in range(int(input())):
    marchands.append(int(input()))


for i in range(len(marchands)):
    print(marchands.index(i))
