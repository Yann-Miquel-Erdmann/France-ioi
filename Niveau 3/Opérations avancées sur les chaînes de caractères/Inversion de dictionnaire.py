# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=556&idTask=2425

mots = []

for i in range(int(input())):
    mots.append((input().split(" ")[::-1]))

mots.sort(key=lambda mot: mot[0])

print("\n".join([" ".join(mot) for mot in mots]))
