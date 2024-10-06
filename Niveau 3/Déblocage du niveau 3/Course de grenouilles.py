# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=656&idTask=2279

nbGrenouilles = int(input())
nbTours = int(input())

points = [0 for i in range(nbGrenouilles)]
tete = [0 for i in range(nbGrenouilles)]

for i in range(nbTours):
    if len([a for a, j in enumerate(points) if j == max(points)]) == 1:
        tete[points.index(max(points))] += 1
    gre, pts = input().split(" ")
    gre, pts = int(gre), int(pts)
    points[gre-1] += pts


print(tete.index(max(tete))+1)
