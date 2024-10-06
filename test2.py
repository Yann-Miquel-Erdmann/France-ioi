import time
dico = {}

t = time.time()
count = 0
for i in range(1_000_000):
    dico[i] = i
    if i in dico.keys():
        count+=1
print(count)
print(time.time()-t)


t = time.time()
count = 0
keyset = set()
for i in range(1_000_000):
    dico[i] = i
    keyset.add(i)
    if i in keyset:
        count+=1
print(count)
print(time.time()-t)