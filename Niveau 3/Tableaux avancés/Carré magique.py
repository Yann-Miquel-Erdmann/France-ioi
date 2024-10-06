# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=564&idTask=469

matrix = []
cote = int(input())
for i in range(cote):
    matrix.append(list(map(int, input().split())))

somme = sum(matrix[0])
vrai = True
linesum = [sum(line) for line in matrix]
columnsum = [0 for i in range(cote)]
diagsum = [0, 0]


for l, line in enumerate(matrix):
    diagsum[0] += matrix[l][l]
    diagsum[1] += matrix[(cote - 1) - l][l]

    for e, elem in enumerate(line):
        columnsum[e] += elem


# print(linesum)
# print(columnsum)
# print(diagsum)

columnsum = [True if elem == somme else False for elem in columnsum]
linesum = [True if elem == somme else False for elem in linesum]
diagsum = [True if elem == somme else False for elem in diagsum]

# print(linesum)
# print(columnsum)
# print(diagsum)


vrai = vrai and all(columnsum)
vrai = vrai and all(linesum)
vrai = vrai and all(diagsum)


flatmatrix = sum(matrix, [])
for i in range(cote**2):
    vrai = vrai and i + 1 in flatmatrix

print("yes" if vrai else "no")
