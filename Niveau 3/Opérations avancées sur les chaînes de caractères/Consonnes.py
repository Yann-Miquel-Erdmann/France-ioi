# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=556&idTask=1720

print(
    " ".join(
        [
            lettre
            for lettre in [
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g",
                "h",
                "i",
                "j",
                "k",
                "l",
                "m",
                "n",
                "o",
                "p",
                "q",
                "r",
                "s",
                "t",
                "u",
                "v",
                "w",
                "x",
                "y",
                "z",
            ]
            if lettre not in "aeyuio"
        ]
    )
)
