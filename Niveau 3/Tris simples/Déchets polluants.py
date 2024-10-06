# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=525&idTask=804

def main():
    nbdechets, lencamion = map(int, input().split(" "))
    dechets = list(map(int, input().split(" ")))
    # dechets = [i for i in range(0, 5000)]
    camion = []
    for i in range(lencamion):

        camion.append(dechets.pop(dechets.index(max(dechets))))

    print(" ".join(map(str, camion)))


main()
