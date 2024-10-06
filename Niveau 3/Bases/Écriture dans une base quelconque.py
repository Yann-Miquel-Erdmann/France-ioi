# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=565&idTask=1748

nombre, base = list(map(int, input().split(" ")))

first = 0
while base ** (first + 1) <= nombre:
    first += 1

valeurs = []
for i in range(first, -1, -1):
    if base**i <= nombre:
        fois = nombre // base**i
        nombre = nombre % base**i
        valeurs.append(fois)
    else:
        valeurs.append(0)

print(len(valeurs))
print(" ".join(map(str, valeurs)))
