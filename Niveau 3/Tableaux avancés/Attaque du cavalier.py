# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=564&idTask=471

plateau = []
for i in range(8):
    plateau.append(list(input()))

moves = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]


def caneat(y, x):
    if x in range(0, 8) and y in range(0, 8):
        if plateau[y][x].islower():
            # print(x, y)
            return True
        else:
            False


result = False

for l, line in enumerate(plateau):
    for e, elem in enumerate(line):
        if elem == "C":
            for movex, movey in moves:
                result = result or caneat(l + movey, e + movex)


print("yes" if result else "no")
