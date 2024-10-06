# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=556&idTask=2423

livres = []
for i in range(int(input())):
    livres.append(input())

livres.sort()

print("\n".join(livres))
