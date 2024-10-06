# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=528&idTask=1171

mot = "a"*1
# mot = "mollakayakokomassa"
# mot = "mqabaqq"
# import string
# import random

# mot = "".join(random.choice(string.ascii_lowercase) for i in range(10000))
# print(mot)

# mot  = "aabbab"

mot = input()
bestcount = 1   



def cherche_pair(i):
    global bestcount
    mn = min(i, len(mot)-i-2)
    for j in range(1,mn+1):
        if mot[i-j] != mot[i+1+j]:
            mx = i+j-(i-j)
            if mx > bestcount:

                bestcount = mx
            return
    mx = (i+mn+1)-(i-1-mn)   
    if mx > bestcount:

        bestcount = mx


def cherche_impair(i):
    global bestcount
    mn = min(i-1, len(mot)-i-2)
    for j in range(1,mn+1):
        if mot[i-1-j] != mot[i+1+j]:


            mx = (i+1+j)-(i-j)
            if mx > bestcount:

                bestcount = mx
            return
            
    mx = (i+2+mn)-(i-1-mn) 


    if mx > bestcount:

        bestcount = mx
        
if len(mot) != 1:

    if mot[0] == mot[1]:
        cherche_pair(0)

    for i in range(1,len(mot)-1):
        if mot[i] == mot[i+1]:
            cherche_pair(i)
        if mot[i-1] == mot[i+1]:
            cherche_impair(i)
        
        if bestcount == len(mot):
            break

print(bestcount)
