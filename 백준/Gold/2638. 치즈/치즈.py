def cheesepad(matrix):
    global delta,col,row
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    col,row = len(matrix),len(matrix[0])
    cury,curx = 0,0
    stack = []
    while True:
        for look in delta:
            looky,lookx = cury+look[0],curx+look[1]
            if 0<=looky<col and 0<=lookx<row and matrix[looky][lookx]==0:
                matrix[looky][lookx] = 2
                stack.append([looky,lookx])
        if len(stack)==0:
            return matrix
        else:
            [cury,curx] = stack.pop()
            
def cheese(matrix):
    matrix_copy = [[j for j in i] for i in matrix]
    for c in range(1,col-1):
        for r in range(1,row-1):
            if matrix[c][r]==1:
                cury,curx = c,r
                airstack = 0
                for look in delta:
                    looky,lookx = cury+look[0],curx+look[1]
                    if matrix[looky][lookx]==2:
                        airstack += 1
                if airstack>=2:
                    matrix_copy[cury][curx] = 2
                else:
                    matrix[cury][curx] = 3
                findcheese = True
                stack = []
                while findcheese==True:
                    airstack = 0
                    for look in delta:
                        looky,lookx = cury+look[0],curx+look[1]
                        if matrix[looky][lookx]==1:
                            stack.append([looky,lookx])
                            matrix[looky][lookx] = 3
                        elif matrix[looky][lookx]==2:
                            airstack += 1
                    if airstack>=2:
                        matrix_copy[cury][curx] = 2
                    if len(stack)==0:
                        findcheese = False
                    else:
                        [cury,curx] = stack.pop()
    return matrix_copy

matrix = []
for i in range(int(input().split()[0])):
    matrix.append(list(map(int,input().split())))
    
iszero = True
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            iszero = False
if iszero == True:
    print(0)
else:            
    time = 0
    while True:
        iszero = True
        matrix = cheese(cheesepad(matrix))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 2:
                    matrix[i][j] = 0
                elif matrix[i][j] == 1:
                    iszero = False
        time += 1
        if iszero == True:
            break
    print(time)