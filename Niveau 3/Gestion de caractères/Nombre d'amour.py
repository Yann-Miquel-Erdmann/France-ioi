# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=566&idTask=2415

prenom_un, prenom_deux = input().split(" ")
alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


points = [0, 0]
for char in prenom_un:
    points[0] += alph.index(char)
print(points[0])
while points[0] >= 10:

    lst = [int(a) for a in str(points[0])]
    points[0] = 0
    for i in lst:
        points[0] += i

for char in prenom_deux:
    points[1] += alph.index(char)
print(points[1])
while points[1] >= 10:
    lst = [int(a) for a in str(points[1])]
    points[1] = 0
    for i in lst:
        points[1] += i

print(points[0], points[1])
