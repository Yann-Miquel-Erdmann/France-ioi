# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=762&idTask=906

import time
import random


K,N = list(map(int,input().split()))


matrix = [[-1 for _ in range(K)] for _ in range(K)]
to_visit_x = []
to_visit_y = []
for _ in range(N):
    # x,y = map(int, input().split())
    # to_visit_x.append(x)
    # to_visit_y.append(y)


    to_visit_x.append(random.randint(0, K-1))
    to_visit_y.append(random.randint(0, K-1))


    matrix[to_visit_y[-1]][to_visit_x[-1]] = 0


to_visit_x,to_visit_y =  [list(t) for t in zip(*list(set(zip(to_visit_x,to_visit_y))))]



t = time.perf_counter()

max_dist = 0


for visit_id in range(K**2):
    val = matrix[to_visit_y[visit_id]][to_visit_x[visit_id]]+1

    if to_visit_x[visit_id] != K-1:
        if matrix[to_visit_y[visit_id]][to_visit_x[visit_id]+1] == -1:
            matrix[to_visit_y[visit_id]][to_visit_x[visit_id]+1] = val
            if val > max_dist:
                max_dist = val
            to_visit_x.append(to_visit_x[visit_id]+1)
            to_visit_y.append(to_visit_y[visit_id])

    if to_visit_y[visit_id] != K-1:
        if matrix[to_visit_y[visit_id]+1][to_visit_x[visit_id]] == -1:
            matrix[to_visit_y[visit_id]+1][to_visit_x[visit_id]] = val
            if val > max_dist:
                max_dist = val
            to_visit_x.append(to_visit_x[visit_id])
            to_visit_y.append(to_visit_y[visit_id]+1)


    if to_visit_x[visit_id] != 0:
        if matrix[to_visit_y[visit_id]][to_visit_x[visit_id]-1] == -1:
            matrix[to_visit_y[visit_id]][to_visit_x[visit_id]-1] = val
            if val > max_dist:
                max_dist = val
            to_visit_x.append(to_visit_x[visit_id]-1)
            to_visit_y.append(to_visit_y[visit_id])

    if to_visit_y[visit_id] != 0:
        if matrix[to_visit_y[visit_id]-1][to_visit_x[visit_id]] == -1:
            matrix[to_visit_y[visit_id]-1][to_visit_x[visit_id]] = val
            if val > max_dist:
                max_dist = val
            to_visit_x.append(to_visit_x[visit_id])
            to_visit_y.append(to_visit_y[visit_id]-1)
    
    



print(max_dist)
print(len(to_visit_x))
print(time.perf_counter()-t)
    


# print("\n".join((" ".join(map(str,elem)) for elem in matrix]))

