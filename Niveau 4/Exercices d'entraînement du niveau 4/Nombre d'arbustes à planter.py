# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=762&idTask=243

lignes,colones = list(map(int,input().split()))

lab = [input().count("#") for i in range(lignes)]

print(sum(lab))
