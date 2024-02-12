def rainy(matrix):
    delta = [(0,1),(1,0),(-1,0),(0,-1)]
    col,row = len(matrix),len(matrix[0])
    cnt = 0
    for c in range(col):
        for r in range(row):
            if matrix[c][r]>0:
                cury,curx = c,r
                matrix[cury][curx] = 0
                stack = []
                checking = True
                while checking == True:
                    for look in delta:
                        looky,lookx = cury+look[0],curx+look[1]
                        if 0<=looky<col and 0<=lookx<row and matrix[looky][lookx]>0:
                            matrix[looky][lookx] = 0
                            stack.append([looky,lookx])
                    if len(stack)==0:
                        cnt+=1
                        checking = False
                    else:
                        [cury,curx] = stack.pop()
    return cnt

col = int(input())
matrix = []
for c in range(col):
    matrix.append(list(map(int,input().split())))

#1부터 100이 될 때까지 matrix의 각 원소들을 1씩 뺌
#cnt를 배열에 추가
#cnt가 0이 될 경우 중지

cntlist = []
for i in range(0,101):
    matrix_copy = [[j-i for j in k] for k in matrix]
    temp = rainy(matrix_copy)
    cntlist.append(temp)
    if temp == 0:
        break
print(max(cntlist))