# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=762&idTask=1130


# import random

# M = 100
# chansons = "".join([f'{random.randint(0, M/10)}  ' for i in range(M)])
# print(str(chansons))
# chansons = list(map(lambda elem:elem.split(),chansons.split(" 0")))
# print(str(chansons))


M = int(input())
chansons = list(map(lambda elem:elem.split(),input().split(" 0")))
print(max(map(len,map(set,chansons))))
