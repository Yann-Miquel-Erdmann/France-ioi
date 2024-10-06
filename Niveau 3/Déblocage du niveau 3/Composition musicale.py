# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=656&idTask=2240

morceau = str(input())
notes = ["aa", "bb", "cc", "dd", "ee", "ff", "gg"]
modif = True
while modif:
    modif = False
    for note in notes:
        lst = morceau.split(note)
        if len(lst) > 1:
            modif = True
            morceau = ""
            for i in lst:
                if i not in notes:
                    morceau += i
print(morceau)
