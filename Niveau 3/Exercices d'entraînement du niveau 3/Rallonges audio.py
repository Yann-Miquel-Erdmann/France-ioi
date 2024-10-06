# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=761&idTask=874

listes = [[], []]
longueurFinale = 0
for i in range(int(input())):
    a, b, longueur = list(map(int, input().split(" ")))
    if a and b:
        listes[0].append(longueur)
    elif not a and not b:
        listes[1].append(longueur)
    else:
        longueurFinale += longueur

if len(listes[0]):
    listes[0].sort()
    listes[1].sort()
    longueurFinale += listes[0].pop()

    for i in range(min(map(len, listes))):
        longueurFinale += listes[0].pop() + listes[1].pop()

    print(longueurFinale)
else:
    print(-1)
