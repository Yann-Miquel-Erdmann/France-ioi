# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=509&idTask=581

largeur = int(input())
longueur = int(input())
motif = input()
for i in range(largeur):
    print("".join([motif] * longueur))
