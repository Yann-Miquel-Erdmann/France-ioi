# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=513&idTask=511

valeur, nombre = list(map(int, input().split(" ")))


def encadrer(valeur, max, i):
    if i < max:
        encadrer([valeur], max, i + 1)
    else:
        print(valeur)


encadrer(valeur, nombre, 0)
