# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=595&idTask=2405

maximum = 0

for i in range(int(input())):
    livre = input()
    if len(livre) > maximum:
        maximum = len(livre)
        print(livre)
