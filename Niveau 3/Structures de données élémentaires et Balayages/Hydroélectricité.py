# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=527&idTask=921

centrale, longueur = list(map(int, input().split(" ")))

riviere = list(map(int, input().split(" ")))

s = sum(riviere[0:centrale])
maximum = s
for i in range(1, longueur - centrale):
    print(i)
    s = s - riviere[i - 1] + riviere[i + centrale - 1]
    if s > maximum:
        maximum = s

print(maximum)
