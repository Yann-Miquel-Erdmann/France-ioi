# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=651&idTask=2073

nbProduits = int(input())
nbPersonnes = int(input())

produits = []
for i in range(nbProduits):
    produits.append(0)

for i in range(nbPersonnes):
    produits[int(input())] += 1

for i in produits:
    print(i)
