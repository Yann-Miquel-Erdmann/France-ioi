# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=651&idTask=2074

charges = []
charge_totale = 0

longueur = int(input())
for i in range(longueur):
    charge = float(input())
    charges.append(charge)
    charge_totale += charge

charge_moyenne = charge_totale / longueur
for charge in charges:
    print(charge_moyenne - charge)
