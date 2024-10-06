# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=556&idTask=2420

print(
    (lambda tic, texte: len([mot for mot in texte.lower().split(" ") if mot == tic]))(
        input(), input()
    )
)
