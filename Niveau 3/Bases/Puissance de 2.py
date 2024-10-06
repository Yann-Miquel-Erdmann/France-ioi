# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=565&idTask=440

nombre = int(input())

puissance = 0
while 2 ** (puissance + 1) < nombre:
    puissance += 1

print(2**puissance)
