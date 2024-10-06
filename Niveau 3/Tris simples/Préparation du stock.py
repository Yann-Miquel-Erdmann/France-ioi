# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=525&idTask=803

import sys


def main():
    nbdechets, nbnewdechets = map(int, input().split(" "))
    dechets = list(map(int, input().split(" ")))
    newdechets = list(map(int, sys.stdin.readline().split()))
    inserts = []
    for newdechet in newdechets:
        for i, dechet in enumerate(dechets):
            if newdechet <= dechet:
                dechets.insert(i, newdechet)
                inserts.append(i)
                break
        else:
            inserts.append(len(dechets))
            dechets.append(newdechet)

    print(" ".join(map(str, inserts)))
    print(" ".join(map(str, dechets)))


main()
