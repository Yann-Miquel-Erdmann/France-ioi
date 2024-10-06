# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=556&idTask=2424

dernier = ""

for i in range(int(input())):
    livre = input()
    if livre > dernier:
        dernier = livre
        print(livre)
