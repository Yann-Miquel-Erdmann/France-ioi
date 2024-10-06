# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=648&idTask=496

for i in range(int(input())):
    x, y = int(input()), int(input())

    if (x <= 0 or x > 90) or (y <= 0 or y > 70):
        print("En dehors de la feuille")
    elif ((10 < x and x < 85) and (10 < y and y < 55))and(not((25 < x and x < 50) and (20 < y and y < 45))):
        print("Dans une zone bleue")
    elif ((15 < x and x < 45) and (60 < y and y < 70))or((60 < x and x < 85) and (60 < y and y < 70)):
        print("Dans une zone rouge")
    else:
        print("Dans une zone jaune")
