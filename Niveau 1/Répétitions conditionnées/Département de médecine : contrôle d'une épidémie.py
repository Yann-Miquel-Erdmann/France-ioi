# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=649&idTask=2051

pop = int(input())
infect = 1
jour = 1
while infect < pop:
    infect = infect*3
    jour += 1
print(jour)
