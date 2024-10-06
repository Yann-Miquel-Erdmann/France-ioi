# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=533&idTask=245

# L,C = list(map(int,input().split(" ")))
# Rl,Rc=range(L),range(C)
# matrix = [input() for i in range(L)]


L,C = 4,5
Rl,Rc=range(L),range(C)
matrix =   ["#"*C,"."*(C-1)+"#",]+[f"#{'.'*(C-2)}#" for i in range(L-3)]+["#"*(C-2)+"."+"#",]

print(matrix)

count = 0

def search(point,visited):
    global count,L,C
    # print(point)
    if point == (C-2,L-1):
        count +=1
        return
    
    visited.add(point)
    for i in [-1,1]:
        m = (point[0]+i,point[1])
        if m not in visited:
            if m[0] in Rc:
                if matrix[m[1]][m[0]] == ".":
                    search(m, set(visited))
        
    for j in [-1,1]:
        m = (point[0],point[1]+j)
        if  m not in visited:
            if m[1] in Rl:
                if matrix[m[1]][m[0]] == ".":
                    search(m, set(visited))
        


search((0,1), set())

print(count)
