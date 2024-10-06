# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=565&idTask=441

nombre = int(input())
first = int(nombre**0.5)

res = 0

for i in range(first, -1, -1):
    if 2**i <= nombre:
        nombre -= 2**i
        res *= 10
        res += 1
    else:
        res *= 10

print(res)
