# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=762&idTask=374

codes = int(input())
elements = list(map(int,input().split()))


ct = [0 for i in range(codes+1)]
for elem in elements:
    ct[elem]+=1
print(max(ct))
