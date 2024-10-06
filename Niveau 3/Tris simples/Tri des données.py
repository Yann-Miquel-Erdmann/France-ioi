# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=525&idTask=805

import sys


def main():

    nbdechets = int(sys.stdin.readline())
    dechets = list(map(int, sys.stdin.readline().split()))
    newlist = []

    for i in range(nbdechets):
        newlist.append(dechets.pop(dechets.index(min(dechets))))

    print(" ".join(map(str, newlist)))


main()
