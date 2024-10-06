# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=761&idTask=752

nombrepetit = int(input())
petits = list(map(int, input().split(" ")))

nombresouple = int(input())
souples = list(map(int, input().split(" ")))

total = petits + souples
total.sort()
n = 0
for i in range(len(total) - 1):
    if total[i] == total[i + 1]:
        n += 1

print(n)
