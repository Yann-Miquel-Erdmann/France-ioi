# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=534&idTask=362

N = int(input())
nombres = [input()[-4:] for i in range(N)]

# import sys,time
# t = time.perf_counter()
# N = 10000
# nombres = [str(sys.maxsize)[-4:] for i in range(N)]
# print(nombres)


resultat = nombres[0]
for nombre in nombres[1:]:
    resultat = str(int(resultat)*int(nombre))[-4:]
print("{:04d}".format(int(resultat)))

