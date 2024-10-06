# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=651&idTask=2078

entiers = []
for i in range(int(input())):
    entiers.append(int(input()))

entiers.sort()

for i in range(int(len(entiers) / 2)):
    print(entiers[i], entiers[-i - 1])
