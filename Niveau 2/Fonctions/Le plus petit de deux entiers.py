# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=509&idTask=1717

nombres = [int(input()) for i in range(10)]

petit = 10000
for nombre in nombres:
    if nombre < petit:
        petit = nombre

print(petit)
