# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=595&idTask=2412

jeu1 = list(input())
jeu2 = list(input())

egalites = 0
gagnant = "="

if len(jeu1) > len(jeu2):
    gagnant = 1
if len(jeu1) < len(jeu2):
    gagnant = 2
while len(jeu1) > 0 and len(jeu2) > 0:
    lettre1 = jeu1.pop(0)
    lettre2 = jeu2.pop(0)

    if lettre1 < lettre2:
        gagnant = 1
        break

    if lettre1 > lettre2:
        gagnant = 2
        break

    if lettre1 == lettre2:

        egalites += 1


print(gagnant)
print(egalites)
