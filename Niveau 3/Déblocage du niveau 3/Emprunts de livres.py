# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=656&idTask=2273

nbLivres, nbJours = map(int, input().split())

livres = []
for o in range(nbLivres):
    livres.append(0)

for i in range(nbJours):
    for a in range(int(input())):
        lv, jours = map(int, input().split())
        if livres[lv] <= i:
            livres[lv] = jours+i
            print(1)
        else:
            print(0)
