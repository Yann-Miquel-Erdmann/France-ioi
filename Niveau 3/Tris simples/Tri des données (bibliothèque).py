# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=525&idTask=751

import sys


def main():

    nbdechets = int(sys.stdin.readline())
    dechets = list(map(int, sys.stdin.readline().split()))
    dechets.sort()
    print(" ".join(map(str, dechets)))


main()
