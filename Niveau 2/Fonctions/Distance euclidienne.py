# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=509&idTask=1718

from math import *

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

N, R = str(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)).split(".")
print(N + "." + R[0:6])
