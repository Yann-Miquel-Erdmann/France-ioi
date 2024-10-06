# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=656&idTask=2278

nbMesures = int(input())
diffMax = float(input())


def diffabs(liste):
    diff = 0
    for i in range(len(liste)-1):
        if abs(liste[i]-liste[i+1]) > diff:
            diff = abs(liste[i]-liste[i+1])
    return diff


mesures = []
for i in range(nbMesures):
    mesures.append(float(input()))

tours = 0
while diffabs(mesures) >= diffMax:
    newmesures = []
    newmesures.append(mesures[0])
    for i in range(1, nbMesures-1):
        newmesures.append((mesures[i-1]+mesures[i+1])/2)
    newmesures.append(mesures[nbMesures-1])
    mesures = newmesures
    tours += 1
print(tours)
