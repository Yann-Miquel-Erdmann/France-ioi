# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=565&idTask=442

nombre = input()

resultat = 0
for i, bit in enumerate(nombre[::-1]):
    resultat += int(bit) * 2**i

print(resultat)
