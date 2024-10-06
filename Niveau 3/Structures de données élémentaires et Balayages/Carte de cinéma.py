# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=527&idTask=1796

import sys

import time


def main():

    # nbclients = int(sys.stdin.readline())
    # clients = list(map(int, sys.stdin.readline()[:-1].split()))

    nbclients = 4
    clients = [1, 3, 2, 2, 1, 3, 3]
    # nbclients = 1000000
    # clients = [i for i in range(nbclients - 1)] + [nbclients - 1]
    # t = time.time()
    newclients = clients[:]
    newclients.sort()

    doubles = []
    for i in range(nbclients):
        if newclients[i] == newclients[(i + 1) % (nbclients)]:
            doubles.append(newclients[i])

    if len(doubles) > 0:
        if len(doubles) == 1:
            print(clients[doubles[0]])

        else:
            doubles = [
                [i for i, elem in enumerate(clients) if elem == double]
                for double in doubles
            ]
            print(doubles)

            for double in doubles:
                for test in doubles:

                    if test[0] < double[1] and test[1] < double[1]:
                        print(clients[test[1]])
                        break

    else:
        print(-1)


main()
