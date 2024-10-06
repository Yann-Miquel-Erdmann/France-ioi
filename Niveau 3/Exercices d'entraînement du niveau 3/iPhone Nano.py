# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=761&idTask=1120

dictionnaire = []

for i in range(int(input())):
    dictionnaire.append(input())

lettres = int(input())
possiblilites = [mot for mot in dictionnaire if len(mot) == lettres]
for i in range(lettres):
    l = input()
    newpossiblilites = []
    for mot in possiblilites:
        if mot[i] in l:
            newpossiblilites.append(mot)
    possiblilites = newpossiblilites
print(possiblilites[0])
