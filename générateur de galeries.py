import time


t = time.perf_counter()
l,h = 1000,1001

matrix = []
for i in range(h):
    if i%2 == 0:
        matrix.append([0]*l)
    else:
        matrix.append([0 if (a == 0 and i%4 == 3) or (a == l-1 and i%4 == 1) else 1 for a in range(l)])
print(time.perf_counter()-t)


# # print(matrix)
# with open("maze.txt","w") as o:
#     o.write("\n".join([" ".join(map(str,elem)) for elem in matrix]))


