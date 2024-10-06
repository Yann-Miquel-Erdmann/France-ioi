# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=527&idTask=355

from zlib import DEFLATED


import sys


def main():

    nbproduits = int(sys.stdin.readline())
    produits = list(map(int, sys.stdin.readline()[:-1].split()))
    for i in range(int(sys.stdin.readline())):
        id, change = list(map(int, sys.stdin.readline()[:-1].split()))
        produits[id - 1] += change

    print(" ".join(map(str, produits)))


main()
