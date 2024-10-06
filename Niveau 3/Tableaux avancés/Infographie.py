# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=564&idTask=1792

lin, col = map(int, input().split(" "))
matrix = []

for i in range(lin):
    matrix.append(["."] * col)

for i in range(int(input())):
    y1, x1, y2, x2, val = input().split(" ")
    y1, x1, y2, x2 = map(int, [y1, x1, y2, x2])
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            matrix[y][x] = val

print("\n".join(["".join(elem) for elem in matrix]))
