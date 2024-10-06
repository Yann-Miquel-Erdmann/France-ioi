# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=762&idTask=749

import sys
# import time, random


H, P, N = list(map(int, input().split()))

t = time.perf_counter()
glissant = [0 for _ in range(H-1)]
somme_glissante = 0
for i in range(N):
    val = int(input())
    # val = random.randint(0, H)
    if somme_glissante+val <= P:
        glissant.append(val)
        somme_glissante += val
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
        glissant.append(0)
        
    somme_glissante -= glissant[i]
    import sys
