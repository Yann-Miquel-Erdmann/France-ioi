# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=525&idTask=753

import sys


def main():

    dechets = []

    for i in range(int(sys.stdin.readline())):
        dechets.append(sys.stdin.readline()[:-1])

    dechets.sort()

    print("\n".join(dechets))


main()
