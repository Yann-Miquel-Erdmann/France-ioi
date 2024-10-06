# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=648&idTask=1982

taille = 177
age = 33
poids = 70
cheval = 0
brun = 0

if cheval == 0:
    print("yes")

counter = 0

if 178 <= taille and taille <= 182:
    counter += 1
if age >= 34:
    counter += 1
if poids < 70:
    counter += 1
if cheval < 1:
    counter += 1
if brun == 1:
    counter += 1


if counter == 5:
    print("Très probable")
elif counter > 2:
    print("Probable")
elif counter == 0:
    print("Impossible")
else:
    print("Peu probable")
