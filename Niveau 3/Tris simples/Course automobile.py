# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=525&idTask=1791

import sys


def main():
    croisements = []
    nbvoitures = int(sys.stdin.readline())
    voitures = list(map(int, sys.stdin.readline().split()))
    for i in range(nbvoitures):
        for a in range(voitures.index(i + 1), i, -1):
            croisements.append((voitures[a - 1], voitures[a]))
            temp = voitures[a - 1]
            voitures[a - 1] = voitures[a]
            voitures[a] = temp
    print(len(croisements))
    print("\n".join([" ".join(map(str, elem)) for elem in croisements]))


main()
