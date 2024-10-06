# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=650&idTask=1996

from math import *
oldTaxe = float(input())
newTaxe = float(input())
prix = float(input())

init = prix*(100/(100+oldTaxe))
final = init*(1+newTaxe/100)
print(round(final*100)/100)
