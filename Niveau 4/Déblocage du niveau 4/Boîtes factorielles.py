# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=671&idTask=2331

nbPetitsPois = int(input())

factorials = [479001600, 39916800, 3628800,	362880, 40320, 5040, 720, 120, 24, 6, 2, 1]


lst = []
start = 0
for fact in factorials:
    num = nbPetitsPois//fact
    if num != 0 or start == 1:
        lst.insert(0, num)
        nbPetitsPois -= fact*num
        start = 1

print(len(lst))
print(''.join(str(e)+" "for e in lst))
