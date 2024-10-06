# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=650&idTask=2463

zones = int(input())

res = zones % 24

if res >= 0:
    print(0+res)
else:
    print(25-res)
