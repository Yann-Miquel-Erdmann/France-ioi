# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=509&idTask=461

counter = 0


def wait_code():
    global counter
    print("Entrez le code :")

    valeur = input()
    if valeur == "4242" and counter == 0:
        counter += 1
        print("Premier code bon.")
        wait_code()
        return

    if valeur == "2121" and counter == 1:
        print("Bravo.")
        return
    else:
        wait_code()


wait_code()
