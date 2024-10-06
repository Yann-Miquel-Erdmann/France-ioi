# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=761&idTask=1121

L, C = list(map(int, input().split(" ")))
matrix = [list(input()) for _ in range(L)]
moves = int(input())
moveslist = list(input())

billes = [(x, y) for x in range(C) for y in range(L) if matrix[y][x] == "x"]

out = set()

def pencher(direction):
    mvt = (0,0)
    if direction == "S":
        billes.sort(key=(lambda elem: elem[1] * -1))
        mvt = (0,1)

    if direction == "N":
        billes.sort(key=(lambda elem: elem[1]))
        mvt = (0,-1)

    if direction == "E":
        billes.sort(key=(lambda elem: elem[0] * -1))
        mvt = (1,0)

    if direction == "O":
        billes.sort(key=(lambda elem: elem[0]))
        mvt = (-1,0)

    to_remove = set()
    for i,bille in enumerate(billes):
        if (bille[0], bille[1], direction) in out:
            to_remove.add(bille)
            matrix[bille[1]][bille[0]] = "."
        
        ct = 1
        while matrix[bille[1]+mvt[1]*ct][bille[0]+mvt[0]*ct] == ".":
            if (bille[0]+mvt[0]*ct, bille[1]+mvt[1]*ct, direction) in out:
                to_remove.add(bille)
                matrix[bille[1]][bille[0]] = "."
                new = {(bille[0]+i*mvt[0], bille[1]+i*mvt[1], direction) for i in range(ct)}
                out.update(new)
            ct+=1
        else:
            if matrix[bille[1]+mvt[1]*ct][bille[0]+mvt[0]*ct] == "O":
                to_remove.add(bille)
                matrix[bille[1]][bille[0]] = "."
                new = {(bille[0]+i*mvt[0], bille[1]+i*mvt[1], direction) for i in range(ct)}
                out.update(new)
            else:
                if ct != 1:
                    matrix[bille[1]][bille[0]] = "."
                    matrix[bille[1]+mvt[1]*(ct-1)][bille[0]+mvt[0]*(ct-1)] = "x"
                    billes[i] = (bille[0]+mvt[0]*(ct-1),bille[1]+mvt[1]*(ct-1))

        
    for bille in to_remove:
        billes.remove(bille)

for move in moveslist:
    pencher(move)

    # print(move)
    # print("\n".join(["".join(elem) for elem in matrix]))
    # print()

print(len(billes))


"""
7 8
########
#x..x.O#
#....O.#
#...x#.#
####O#.#
#Ox..#x#
########
4
SEWN

"""