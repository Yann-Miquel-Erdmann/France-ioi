# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=761&idTask=871

n = int(input())
mot = input()


l = n * 2 - 1
matrix = [[mot[-1] for i in range(l)] for a in range(l)]

for a in range(n - 1, 0, -1):
    for b in [int((l - (a * 2 - 1)) / 2), int(l - (l - (a * 2 - 1)) / 2) - 1]:
        for c in range(int((l - (a * 2 - 1)) / 2), int(l - (l - (a * 2 - 1)) / 2)):
            matrix[b][c] = mot[a - 1]

    for b in range(int((l - (a * 2 - 1)) / 2) + 1, int(l - (l - (a * 2 - 1)) / 2) - 1):
        for c in [int((l - (a * 2 - 1)) / 2), int(l - (l - (a * 2 - 1)) / 2) - 1]:
            matrix[b][c] = mot[a - 1]

print("\n".join(["".join(line) for line in matrix]))
