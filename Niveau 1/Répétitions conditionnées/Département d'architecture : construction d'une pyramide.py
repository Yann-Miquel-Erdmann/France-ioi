# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=649&idTask=2052

nb = int(input())

tour = -1
utilise = 0
while utilise+(tour+1)**2 <= nb:
    tour += 1
    utilise += tour**2

print(tour)
print(utilise)
