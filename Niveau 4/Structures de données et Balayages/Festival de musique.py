# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=532&idTask=1800

import bisect
def main():
    jours, groupes = list(map(int,input().split()))
    concerts = list(map(int,input().split()))
    indices = [[] for i in range(groupes)]
    for ind,grp in enumerate(concerts):
        indices[grp-1].append(ind)
    
    any(lst.sort(reverse=1) for lst in indices)

    new = list(map(lambda x: x.pop(),indices))
    new.sort()


    best = jours
    for i in range(jours+1-groupes):

        mn = new[0]
        mx = new[-1]
        mxscore = mx+1- mn
        if best > mxscore:
            best = mxscore
        
        new.pop(0)
        if len(indices[concerts[mn]-1]) != 0:
            bisect.insort(new,indices[concerts[mn]-1].pop())



        else:
            print(best)
            return

    print(best)


main()
