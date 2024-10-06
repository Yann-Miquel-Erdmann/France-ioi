# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=761&idTask=1510

import sys
# import time


def main():
    h, l, d = list(map(int, input().split()))
    matrix = [list(map(int, sys.stdin.readline()[:-1 ].split())) for i in range(h)]

    # matrix = []
    # for i in range(h):
    #     if i%2 == 0 :
    #         matrix.append([0 ]*l)
    #     else:
    #         matrix.append([0  if (a == 0  and i%4 == 3) or (a == l-1  and i%4 == 1 ) else 1  for a in range(l)])
    # t = time.perf_counter()



    d+=1 
    old,new = (0 ,0 ),(0 ,0 )
    fastest = h-1 +l-1 
    count = fastest

    for i in range(1 ,count):
        if new[0] != h-1 :
            if (new[0 ]+1 , new[1 ]) != old:
                if matrix[new[0 ]+1 ][new[1 ]] == 0 :
                    old , new = new , (new[0 ]+1  ,new[1 ])
                    count -=1 
                    if i % d == 0 :
                        sys.stdout.write(str(old[0 ])+" "+str(old[1 ])+"\n")
                    continue

        if new[1 ] != l-1 :
            if (new[0 ], new[1 ]+1 ) != old:
                if matrix[new[0 ]][new[1 ]+1 ] == 0 :
                    old , new = new , (new[0 ] ,new[1 ]+1 )
                    count -=1 
                    if i % d == 0 :
                        sys.stdout.write(str(old[0 ])+" "+str(old[1 ])+"\n")
                    continue

        if new[0 ] != 0 :
            if (new[0 ]-1 , new[1 ]) != old:
                if matrix[new[0 ]-1 ][new[1 ]] == 0 :
                    old , new = new , (new[0 ]-1  ,new[1 ])
                    count +=1 

                    if i % d == 0 :
                        sys.stdout.write(str(old[0 ])+" "+str(old[1 ])+"\n")
                    continue

        if new[1 ] != 0 :
            if (new[0 ], new[1 ]-1 ) != old:
                if matrix[new[0 ]][new[1 ]-1 ] == 0 :
                    old , new = new , (new[0 ],new[1 ]-1 )
                    count +=1 

                    if i % d == 0 :
                        sys.stdout.write(str(old[0 ])+" "+str(old[1 ])+"\n")
                    continue
        
        
    i = fastest-1
    while count != 0:
        i+=1 
        if new[0 ] != h-1 :
            if (new[0 ]+1 , new[1 ]) != old:
                if matrix[new[0 ]+1 ][new[1 ]] == 0 :
                    old , new = new , (new[0 ]+1  ,new[1 ])
                    count -=1 
                    if i % d == 0 :
                        sys.stdout.write(str(old[0 ])+" "+str(old[1 ])+"\n")
                    continue

        if new[1 ] != l-1 :
            if (new[0 ], new[1 ]+1 ) != old:
                if matrix[new[0 ]][new[1 ]+1 ] == 0 :
                    old , new = new , (new[0 ] ,new[1 ]+1 )
                    count -=1 
                    if i % d == 0 :
                        sys.stdout.write(str(old[0 ])+" "+str(old[1 ])+"\n")
                    continue

        if new[0 ] != 0 :
            if (new[0 ]-1 , new[1 ]) != old:
                if matrix[new[0 ]-1 ][new[1 ]] == 0 :
                    old , new = new , (new[0 ]-1  ,new[1 ])
                    count +=1 

                    if i % d == 0 :
                        sys.stdout.write(str(old[0 ])+" "+str(old[1 ])+"\n")
                    continue

        if new[1 ] != 0 :
            if (new[0 ], new[1 ]-1 ) != old:
                if matrix[new[0 ]][new[1 ]-1 ] == 0 :
                    old , new = new , (new[0 ],new[1 ]-1 )
                    count +=1 

                    if i % d == 0 :
                        sys.stdout.write(str(old[0 ])+" "+str(old[1 ])+"\n")
                    continue

    if (i+1) % d == 0:
        sys.stdout.write(str(h-1)+" "+str(l-1)+"\n")
        
    

    # print(time.perf_counter()-t)



if __name__ == "__main__":
    main()


"""
0 0 1 0 0 0 0 0 
1 0 0 0 1 1 1 0 
1 1 1 1 1 0 0 0 
1 0 0 0 1 0 1 1 
1 0 1 0 0 0 1 1 
1 0 1 1 1 1 1 1 
1 0 0 1 1 0 0 0 
1 1 0 0 0 0 1 0 


9 11 6
0 0 0 0 0 0 1 1 1 1 1
1 1 1 1 1 0 1 0 0 0 0
1 1 1 1 1 0 1 0 1 1 0
1 1 1 1 1 0 1 0 1 1 0
1 1 1 1 1 0 1 0 1 1 0
1 1 1 1 1 0 1 0 1 1 0
1 1 1 1 1 0 1 0 1 0 0
1 1 1 1 1 0 1 0 1 0 1
1 1 1 1 1 0 0 0 1 0 0

"""

