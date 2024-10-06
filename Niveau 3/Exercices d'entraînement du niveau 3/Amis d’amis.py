# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=761&idTask=1125

pers = int(input())
proches = set()
pool = set()
for i in range(int(input())):
    p1, p2 = list(map(int, input().split(" ")))
    if p1 == pers:
        proches.add(p2)
    else:
        if p1 in proches:
            if p2 not in proches:
                pool.add(p2)
        else:
            if p2 in proches:
                pool.add(p1)

print(len(pool))
