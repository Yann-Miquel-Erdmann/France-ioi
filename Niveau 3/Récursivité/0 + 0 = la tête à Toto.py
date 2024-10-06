# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=513&idTask=509

def tete(valeur, max, i):
    if i < max:
        tete("(" + valeur + " + " + valeur + ")", max, i + 1)
    else:
        print("0 =", valeur)


tete("0", int(input()), 0)
