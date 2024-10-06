# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=530&idTask=1834

def arrangements(k,j,arr,n):
    lst = []
    for i in range(k-j+1):
        ar = arr[:]
        ar[i+n] = 1
        if j == 1:
            lst.append(ar)
        else:
            lst += arrangements(k-i-1,j-1, ar, i+n+1)
    return lst

