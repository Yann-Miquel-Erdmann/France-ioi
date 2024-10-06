# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=513&idTask=515

def fractale(valeur, max, i):
    if i < max:
        val = [value + value for value in valeur]
        for a in range(len(valeur[0])):
            val.append(valeur[a] + " " * len(valeur[0]))

        fractale(
            val,
            max,
            i + 1,
        )
    else:
        print("\n".join(valeur))


fractale(["#"], int(input()) ** 0.5, 1)
