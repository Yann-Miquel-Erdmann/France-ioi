# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=513&idTask=510

def suivant(nombre, arrivee):
    print(nombre, end=" ")
    if nombre == arrivee:
        return
    suivant(nombre + 1, arrivee)


dep, arr = list(map(int, input().split(" ")))
suivant(dep, arr)
