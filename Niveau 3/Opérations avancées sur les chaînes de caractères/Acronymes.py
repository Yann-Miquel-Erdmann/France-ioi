# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=556&idTask=2421

acronyme = input()
for i in range(int(input())):
    mots = input().lower().split(" ")

    if len(mots) == len(acronyme):

        try:
            for c, mot in enumerate(mots):

                mots[c] = "".join(
                    [
                        lettre.lower() if o != 0 else lettre.upper()
                        for o, lettre in enumerate(mot)
                    ]
                )
                if mots[c][0] != acronyme[0]:
                    raise
            print(" ".join(mots))
        except:
            pass
