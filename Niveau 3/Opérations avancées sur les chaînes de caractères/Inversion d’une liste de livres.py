# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=556&idTask=2422

livres = []

for i in range(int(input())):
    livres.append(input())

for livre in livres[::-1]:
    print(livre)
