# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=595&idTask=2407

nombres = [0] * 100
nombre, mot = map(int, input().split())

for i in range(nombre):
    for mot in input().split(" "):
        nombres[len(mot) - 1] += 1

for i in range(len(nombres)):
    if nombres[i] != 0:
        print("{} : {}".format(i + 1, nombres[i]))
