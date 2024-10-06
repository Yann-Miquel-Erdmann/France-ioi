# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=595&idTask=2410

nom = input()
nombre = 3
if nom < "Q":
    nombre = 2
    if nom < "G":
        nombre = 1

print(nombre)
