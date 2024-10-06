# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=525&idTask=849

import sys


def main():

    dechets = []
    for i in range(int(sys.stdin.readline())):
        dechets.append(tuple(map(int, sys.stdin.readline().split())))

    dechets.sort(key=lambda x: x[0])
    dechets.sort(key=lambda x: x[1])

    print("\n".join([" ".join(map(str, elem)) for elem in dechets]))


main()
