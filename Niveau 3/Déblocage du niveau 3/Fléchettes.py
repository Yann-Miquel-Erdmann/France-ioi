# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=656&idTask=2209

lettres = int(input())
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


stringList = [[0 for i in range(lettres*2-1)]for i in range(lettres*2-1)]


for i in range(lettres):
    for o in range(i, lettres*2-1-i):
        ligne = stringList[o]
        for p in range(i, lettres*2-1-i):

            ligne[p] = alph[i]

        stringList[o] = ligne

for ligne in stringList:
    line = ""
    for char in ligne:
        line += char
    print(line)
