# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=761&idTask=669

nombre = int(input())
liste = list(map(int, input().split(" ")))


liste.sort(key=lambda x: abs(x))

doubles = []
for i in range(len(liste) - 1):
    if liste[i] == liste[i + 1] * -1:
        doubles.append(abs(liste[i]))

doubles = set(doubles)
print(len(doubles))
