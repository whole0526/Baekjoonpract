def getmatrix():
    global col, row
    col,row = map(int,input().split(' '))
    matrix = []
    for _ in range(col):
        matrix.append(list(map(int,input().split(' '))))
    return matrix

def iceberg_melt(matrix):
    global delta
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    matrix_copy = [[i for i in j] for j in matrix]
    for c in range(col):
        for r in range(row):
            if matrix[c][r] == 0:
                for look in delta:
                    if 0 <= c+look[0] < col and 0 <= r+look[1] < row and\
                    matrix_copy[c+look[0]][r+look[1]] != 0:
                        matrix_copy[c+look[0]][r+look[1]] -= 1
    return matrix_copy

def iceberg_cnt(matrix):
    matrix_copy = [[i for i in j] for j in matrix]
    cnticebergnum = 0
    for c in range(1,col-1):
        for r in range(1,row-1):
            if matrix_copy[c][r]!=0:
                cury,curx = c,r
                matrix_copy[cury][curx] = 0
                stack = []
                cnticebergsize = True                
                while cnticebergsize == True:
                    for look in delta:
                        if matrix_copy[cury+look[0]][curx+look[1]] == 0\
                            and matrix_copy[cury][curx] != 0:
                            matrix_copy[cury][curx] -= 1
                    for look in delta:
                        if 1 <= cury+look[0] < col-1 and 1 <= curx+look[1] < row-1 and\
                        matrix_copy[cury+look[0]][curx+look[1]] != 0:
                            matrix_copy[cury+look[0]][curx+look[1]] = 0
                            stack.append([cury+look[0],curx+look[1]])
                    if len(stack) == 0:
                        cnticebergnum += 1
                        cnticebergsize = False
                    else:
                        [cury,curx] = stack.pop()
                if cnticebergnum >= 2:
                    return cnticebergnum #강제 중단
    return cnticebergnum

matrix = getmatrix()

year = 0
while True:
    matrix = iceberg_melt(matrix)
    year+=1
    if iceberg_cnt(matrix)>=2:
        print(year)
        break
    elif iceberg_cnt(matrix) == 0:
        print(0)
        break