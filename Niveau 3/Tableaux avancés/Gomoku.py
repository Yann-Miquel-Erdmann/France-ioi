# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=564&idTask=470

largeur = int(input())
plateau = [list(map(int, input().split(" "))) for i in range(largeur)]
# print(plateau)


def check(direction, x, y, elem):
    for i in range(1, 5):
        xpos = x + direction[0] * i
        ypos = y + direction[1] * i

        if xpos in range(0, largeur) and ypos in range(0, largeur):
            if plateau[ypos][xpos] != elem:
                return 0
        else:
            return 0
    # print(x, y, direction)
    return elem


result = []
for l, line in enumerate(plateau):
    for e, elem in enumerate(line):
        if elem != 0:
            for direction in [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
                (1, 1),
                (-1, 1),
                (1, -1),
                (-1, -1),
            ]:
                res = check(direction, e, l, elem)
                if res != 0:
                    result.append(res)
if len(result) > 0:
    print(result[0])

else:
    print(0)
