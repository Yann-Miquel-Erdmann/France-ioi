# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=595&idTask=2413

lettre = input()
nombre = 0
for i in range(int(input())):
    nombre += len([let for let in input() if let == lettre])

print(nombre)
