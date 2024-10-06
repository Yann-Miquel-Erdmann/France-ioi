# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=528&idTask=1351

import sys

affiches = []

def insertion(liste, valeur):
    if liste[-1]<= valeur:
        liste.pop()
        insertion(liste, valeur)
    else:
        liste.append(valeur)

for i in range(int(sys.stdin.readline())):
    val = sys.stdin.readline()
    if val[0] == "C":
        insertion(affiches, int(val[2:]))

    else:
        print(len(affiches))


