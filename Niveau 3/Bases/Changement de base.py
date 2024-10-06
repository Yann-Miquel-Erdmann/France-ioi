# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=565&idTask=368

basedepart, basearrivee, longeur = list(map(int, input().split(" ")))
valeurs = list(map(int, input().split(" ")))
resultat = 0
for i, bit in enumerate(valeurs[::-1]):
    resultat += int(bit) * basedepart**i


first = 0
while basearrivee ** (first + 1) <= resultat:
    first += 1

final = []
for i in range(first, -1, -1):
    if basearrivee**i <= resultat:
        fois = resultat // basearrivee**i
        resultat = resultat % basearrivee**i
        final.append(fois)
    else:
        final.append(0)

print(" ".join(map(str, final)))
