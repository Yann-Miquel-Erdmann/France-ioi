# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=527&idTask=356

import sys


def main():

    produits = []
    for i in range(int(sys.stdin.readline())):
        nb, date = list(map(int, sys.stdin.readline().split()))
        if nb > 0:
            for o in range(nb):
                produits.append(date)
        else:

            for o in range(-nb):
                produits.pop()

    print(min(produits))


main()
