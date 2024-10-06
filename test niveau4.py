from math import sqrt
import numpy
import time
import copy

nbLignes, nbColonnes = map(int, "10 10".split())
matrix = numpy.random.choice([0, 1], p=[0.9, 0.1], size=(nbLignes, nbColonnes))


t = time.time()
ones = [(x, y) for x in range(nbColonnes) for y in range(nbLignes) if matrix[y][x] == 1]
ones.append((-1, -1))
ones.append((-1, nbLignes))
ones.append((nbColonnes, -1))
ones.append((nbColonnes, nbLignes))


onesX = ones[::-1]
onesY = ones
onesX.sort(key=lambda x: x[0])
onesY.sort(key=lambda x: x[1])


def get_points(point):
    global onesY, onesX
    choseX = [one for one in onesX if one != point]
    choseX.sort(key=lambda x: max(abs(point[1] - x[1]), abs(point[0] - x[0])))
    choseX = [chose for chose in choseX if chose[0] == choseX[0][0]]
    choseX.sort(key=lambda x: x[1])

    choseY = [one for one in onesY if one != choseX[0] and one != point]
    choseY.sort(key=lambda x: max(abs(point[1] - x[1]), abs(point[0] - x[0])))
    choseY = [chose for chose in choseY if chose[1] == choseY[0][1]]

    choseY.sort(key=lambda x: x[0])

    return (
        int(
            min(
                sqrt((point[0] - choseX[0][0]) ** 2 + (point[1] - choseX[0][1]) ** 2),
                sqrt((point[0] - choseY[0][0]) ** 2 + (point[1] - choseY[0][1]) ** 2),
            )
        )
        - 1
    )


maxones = 0
maxpoint = (0, 0)
for one in ones:
    res = get_points(one)
    if res > maxones:
        maxones = res
        maxpoint = one

print(maxones, maxpoint)
print(matrix)
print(time.time() - t)
