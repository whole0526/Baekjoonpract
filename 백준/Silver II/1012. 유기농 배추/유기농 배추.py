def worm(matrix):
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    col,row = len(matrix),len(matrix[0])
    cnt = 0
    for c in range(col):
        for r in range(row):
            if matrix[c][r] == 1:
                cury,curx = c,r
                matrix[cury][curx] = 0
                stack = []
                findcabbage = True
                while findcabbage == True:
                    for look in delta:
                        looky,lookx = cury+look[0],curx+look[1]
                        if 0<=looky<col and 0<=lookx<row and matrix[looky][lookx]==1:
                            stack.append([looky,lookx])
                            matrix[looky][lookx] = 0
                    if len(stack) == 0:
                        cnt+=1
                        findcabbage = False
                    else:
                        [cury,curx] = stack.pop()
    return cnt

for i in range(int(input())):
    row,col,worms = map(int,input().split())
    matrix = [[0]*row for _ in range(col)]
    for j in range(worms):
        temp = list(map(int,input().split()))
        matrix[temp[1]][temp[0]] = 1
    print(worm(matrix))