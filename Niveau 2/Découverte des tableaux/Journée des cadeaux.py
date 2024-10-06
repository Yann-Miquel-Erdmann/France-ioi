# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=651&idTask=2079

richesses = []

for i in range(int(input())):
    richesses.append(int(input()))

richesses.sort()

if len(richesses) % 2 != 0:
    print(richesses[int((len(richesses) - 1) / 2)])
else:
    print(
        (richesses[int(len(richesses) / 2 - 1)] + richesses[int(len(richesses) / 2)])
        / 2
    )
