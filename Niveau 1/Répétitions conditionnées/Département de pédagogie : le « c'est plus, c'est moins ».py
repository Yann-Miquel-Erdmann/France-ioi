# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=649&idTask=2053

goal = int(input())

tour = 1
val = int(input())
while val != goal:
    if val < goal:
        print("c'est plus")
    else:
        print("c'est moins")
    tour += 1
    val = int(input())


print("Nombre d'essais nécessaires :")
print(tour)
