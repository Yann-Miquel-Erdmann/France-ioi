# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=595&idTask=2409

for i in range(int(input())):
    ligne = input()[::-1]
    mots = [mot[::-1] for mot in ligne]
    print("".join(mots))
