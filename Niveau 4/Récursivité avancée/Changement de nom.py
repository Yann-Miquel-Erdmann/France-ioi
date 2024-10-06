# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=530&idTask=358

def rec(mot, n):
    if n == 0:
        print(mot)
        return
    for l in lettres:
        rec(mot+l, n-1)


L = int(input())
lettres = input()
N = int(input())

print(L**N)

rec("",N)

