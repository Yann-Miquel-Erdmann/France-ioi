# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=509&idTask=460

counter = 0


def wait_code():
    global counter
    print("Entrez le code :")
    if input() == "4242":
        counter += 1

        if counter < 2:
            print("Encore une fois.")
            wait_code()
        else:
            print("Bravo.")
            return
    else:
        wait_code()


wait_code()
