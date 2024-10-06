# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=513&idTask=513

def inverser(mot, i, longueur):
    if i > int(longueur / 2):
        print("".join(valeurs))
        return
    l = mot[i]
    mot[i] = mot[longueur - i]
    mot[longueur - i] = l

    inverser(mot, i + 1, longueur)


valeurs = list(input())
inverser(valeurs, 0, len(valeurs) - 1)
