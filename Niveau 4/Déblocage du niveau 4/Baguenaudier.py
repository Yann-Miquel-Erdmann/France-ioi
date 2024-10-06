# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=671&idTask=1504

import time


def Baguenaudier(n):
    # print("bag", n)
    if n==2:
        print(2)
        Baguenaudier(1)
    elif n==1:
        print(1)    
    else:
        Baguenaudier(n-2)
        print(n)
        fonction2(n-1)
        

def fonction2(n):
    if n==1:
        print(1)  
    else:
        fonction2(n-1)
        print(n)
        fonction2(n-1)


Baguenaudier(int(input()))


