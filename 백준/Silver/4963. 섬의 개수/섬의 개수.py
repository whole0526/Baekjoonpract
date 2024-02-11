def island(matrix):
    col,row = len(matrix),len(matrix[0])
    delta = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    cnt = 0
    for starty in range(col):
        for startx in range(row):
            if matrix[starty][startx] == 1:
                matrix[starty][startx] = 0
                cury,curx = starty,startx
                stack = []
                islandsize = True
                while islandsize == True:
                    for rotate in delta:
                        looky,lookx = cury+rotate[0],curx+rotate[1]
                        if 0<=looky<col and 0<=lookx<row and matrix[looky][lookx]==1:
                            stack.append([looky,lookx])
                            matrix[looky][lookx] = 0
                    if len(stack) == 0:
                        cnt += 1
                        islandsize = False
                    else:
                        [cury,curx] = stack.pop()
    return cnt

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    else:
        matrix = []
        for i in range(h):
            matrix.append(list(map(int,input().split())))
    print(island(matrix))