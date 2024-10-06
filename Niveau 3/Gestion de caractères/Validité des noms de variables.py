# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=566&idTask=458

for i in range(int(input())):
    nom = input()
    if nom[0].isalpha() or nom[0] == "_":
        print(
            "YES"
            if sum(
                [
                    0 if char.isalpha() or char.isnumeric() or char == "_" else 1
                    for char in nom
                ]
            )
            == 0
            else "NO"
        )
    else:
        print("NO")
