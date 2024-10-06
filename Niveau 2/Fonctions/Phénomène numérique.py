# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=509&idTask=637

nombre = int(input())


def calcul_suite(terme):
    if terme % 2 == 0:
        return terme / 2
    else:
        return terme * 3 + 1


suite = []

while nombre != 1:
    nombre = int(calcul_suite(nombre))
    suite.append(nombre)

print(" ".join(map(str, suite)))
