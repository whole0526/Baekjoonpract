def picture(matrix):
    delta = [(0,-1),(0,1),(1,0),(-1,0)]
    col,row = len(matrix),len(matrix[0])
    piccnt = []
    for c in range(col):
        for r in range(row):
            if matrix[c][r] == 1:
                stack = []
                cnt = 1
                cury,curx = c,r
                matrix[cury][curx] = 0
                find = True
                while find == True:
                    for look in delta:
                        looky,lookx = cury+look[0],curx+look[1]
                        if 0<=looky<col and 0<=lookx<row and matrix[looky][lookx]==1:
                            matrix[looky][lookx] = 0
                            stack.append([looky,lookx])
                            cnt+=1
                    if len(stack) == 0:
                        piccnt.append(cnt)
                        find = False
                    else:
                        [cury,curx] = stack.pop()
    return piccnt
matrix = []
for col in range(list(map(int,input().split()))[0]):
    matrix.append(list(map(int,input().split())))
temp = picture(matrix)
print(len(temp))
if len(temp) == 0:
    print(0)
else:
    print(max(temp))