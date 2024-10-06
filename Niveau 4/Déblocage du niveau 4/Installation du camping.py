# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=671&idTask=2329

nbLignes, nbColonnes = map(int, input().split())
matrix = [list(map(int, input().split()))for i in range(nbLignes)]
matrix2 = [[0 for a in range(nbLignes+1)] for i in range(nbColonnes+1)]

for y in range(1,nbLignes+1):
    for x in  range(1, nbColonnes+1):
        if matrix[y-1][x-1] == 0:
            matrix2[x][y] = min(matrix2[x-1][y],matrix2[x][y-1],matrix2[x-1][y-1])+1


print(max(list(map(max,matrix2))))
