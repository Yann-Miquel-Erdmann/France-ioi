# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=671&idTask=2330

manteaux = []

for i in range(int(input())):
    a,b = list(map(int,input().split(" ")))
    manteaux.append((a,b))


manteaux.sort(key=lambda x: abs(x[0]-x[1]), reverse=True)

q = 0
while q< len(manteaux)/2:
    m = len(manteaux)
    a,*b = manteaux

    manteaux = [i for i in b if not (i[0]>=a[0] and i[1<=a[1]])] 
    if m-len(manteaux) > q:
        q = m-len(manteaux)
print(q-1)
