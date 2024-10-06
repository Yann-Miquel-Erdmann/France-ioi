# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=595&idTask=2404

livres = int(input())
longueur = int(input())

for i in range(livres):
    titre = input()
    if len(input()) < longueur:
        print(titre)
