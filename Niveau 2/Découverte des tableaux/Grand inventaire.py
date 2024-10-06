# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=651&idTask=2072

tableau = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(int(input())):
    tableau[int(input())-1] += int(input())

for i in tableau:
    print(i)
