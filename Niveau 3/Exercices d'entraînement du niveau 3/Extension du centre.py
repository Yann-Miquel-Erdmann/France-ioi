# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=761&idTask=806

nombre1 = int(input())
centre1 = list(map(int, input().split(" ")))

nombre2 = int(input())
centre2 = list(map(int, input().split(" ")))

centre = centre1 + centre2
centre.sort()
print(" ".join(map(str, centre)))
