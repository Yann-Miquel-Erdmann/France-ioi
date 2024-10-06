# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=649&idTask=2058

nb = int(input())

minTemp = int(input())
maxTemp = int(input())

for i in range(nb):
    temp = int(input())
    if minTemp <= temp and temp <= maxTemp:
        print("Rien à signaler")
    else:
        print("Alerte !!")
        break
