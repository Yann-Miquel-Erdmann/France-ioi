import time
import numpy


def testCase(xC, yC, nbLignes, nbColonnes, matrix, matrix2):

    for cote in range(0, min(nbLignes-yC, nbColonnes-xC)):

        if sum(matrix[yC+cote][xC: xC+cote+1]) != 0:
            return cote
        if sum(matrix2[xC+cote][yC: yC+cote+1]) != 0:
            return cote

    return min(nbLignes-yC, nbColonnes-xC)


def main():

    nbLignes, nbColonnes = map(int, "350 350".split())
    matrix = numpy.random.choice(
        [0, 1], p=[0.999, 0.001], size=(nbLignes, nbColonnes))
    matrix2 = [[matrix[a][i]
                for a in range(nbLignes)] for i in range(nbColonnes)]

    # file_object = open('sample.txt', 'w')
    # for i in matrix:
    #     file_object.write(''.join(str(e)+" "for e in i)+"\n")

    print("start")
    debut = time.time()

    maxC = 0
    y = 0
    while y+maxC < nbLignes:
        for x in range(nbColonnes):
            if x + maxC <= nbColonnes:
                test = testCase(x, y, nbLignes, nbColonnes, matrix, matrix2)
                if test > maxC:
                    maxC = test
        y += 1

    print(maxC)
    print(time.time()-debut)


main()
