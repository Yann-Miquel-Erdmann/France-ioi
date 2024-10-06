# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=556&idTask=2458

somme = 0

while True:
    try:
        somme += sum(map(int, input().split(" ")))
    except:
        break

print(somme)
