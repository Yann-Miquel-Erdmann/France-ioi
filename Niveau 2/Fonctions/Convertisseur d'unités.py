# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=509&idTask=459

for i in range(int(input())):
    valeur, unite = input().split(" ")

    if unite == "m":
        print(float(valeur) / 0.3048, "p")

    if unite == "g":
        print(float(valeur) * 0.002205, "l")

    if unite == "c":
        print(32 + float(valeur) * 1.8, "f")
