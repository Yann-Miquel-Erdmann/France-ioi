# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=564&idTask=1124

from copy import deepcopy
from glob import glob
import time

t = time.time()


def main():

    erosion = int(input())
    height, width = list(map(int, input().split(" ")))

    matrix = [list(input()) for i in range(height)]

    # erosion = 50
    # height, width = 250, 250
    # matrix = [["#" for i in range(width)] for a in range(height)]

    emptyline = ["." for i in range(width)]

    for n in range(erosion):
        newmatrix = deepcopy(matrix)
        newmatrix[n] = emptyline
        newmatrix[height - 1 - n] = emptyline

        for l in range(n + 1, height - n - 1):
            line = matrix[l]
            newmatrix[l][n] = "."
            newmatrix[l][width - 1 - n] = "."
            for e in range(n + 1, width - n - 1):
                elem = line[e]
                if elem == "#":
                    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        xpos = e + direction[0]
                        ypos = l + direction[1]
                        if xpos >= 0 and xpos < width and ypos >= 0 and ypos < height:
                            if matrix[ypos][xpos] != "#":
                                newmatrix[l][e] = "."
                                break

                        else:
                            newmatrix[l][e] = "."
                            break
                    else:
                        newmatrix[l][e] = "#"

        matrix = newmatrix

    # print("\n".join(["".join(elem) for elem in matrix]))


main()

print(time.time() - t)
