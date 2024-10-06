# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=525&idTask=756

from math import ceil, log
import sys
import time


def main():
    nbdechets = int(input())
    t = time.time()

    # nbdechets = 20000
    # dechets = [i for i in range(nbdechets, 0, -1)]
    dechets = list(map(int, input().split()))
    dechets.sort()
    print(dechets)
    n = int(input())
    # for i in range(nbdechets):
    for i in range(n):
        q = int(sys.stdin.readline())
        # q = i

        idlist = [0, int(nbdechets / 2), nbdechets]
        ind = 1

        for a in range(int(ceil(log(nbdechets, 2)))):
            # print("-->", dechets[idlist[ind]])
            if q == dechets[idlist[ind]]:
                print("1")
                break
            elif q > dechets[idlist[ind]]:
                ind += 1
                idlist.insert(ind, int((idlist[ind - 1] + idlist[ind]) / 2))
            elif q < dechets[idlist[ind]]:
                idlist.insert(ind, int((idlist[ind - 1] + idlist[ind]) / 2))

            # print(idlist, ind)

        else:
            print("0")

    print(time.time() - t)


main()
