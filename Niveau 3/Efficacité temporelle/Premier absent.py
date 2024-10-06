# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=528&idTask=1173

from sys import stdin

maximum, nbpresents = list(map(int, input().split(" ")))

presents = set()
absent = 1

for _ in range(nbpresents-1):
    new = int(stdin.readline())
    presents.add(new)
    if new == absent:
        absent+=1
        while absent in presents:
            absent +=1

    
    print(absent)

new = int(stdin.readline())
presents.add(new)
if new == absent:
    absent+=1
    if len(presents) < absent:
        absent = -1
    else:
        while absent in presents:
            absent +=1
if absent > maximum:
    print(-1) 
else:
    print(absent)

