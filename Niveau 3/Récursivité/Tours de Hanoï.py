# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=513&idTask=516

def interchange(valeur):
    if len(valeur[0] or valeur[1]):
        valeur[2].append(valeur[0].pop())
        valeur[1].append(valeur[0].pop())
        valeur[1].append(valeur[2].pop())
        valeur[2].append(valeur[0].pop())
        valeur[0].append(valeur[1].pop())
        valeur[2].append(valeur[1].pop())
        valeur[2].append(valeur[0].pop())
        interchange(valeur)
    else:
        print(valeur)


interchange([[4, 3, 2, 1], [], []])
