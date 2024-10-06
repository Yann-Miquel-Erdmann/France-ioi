# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=565&idTask=1747

basedepart, longeur = list(map(int, input().split(" ")))
valeurs = list(map(int, input().split(" ")))
resultat = 0
for i, bit in enumerate(valeurs[::-1]):
    resultat += int(bit) * basedepart**i

print(resultat)
