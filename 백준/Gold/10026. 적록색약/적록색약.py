def DFS_visitcnt(matrix,yloc,xloc,isblind):

    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    
    stack = []
    currentcolor = [matrix[yloc][xloc]]
    if isblind == True and (currentcolor == ['R'] or currentcolor == ['G']):
        currentcolor = ['R','G']

    matrix[yloc][xloc] = 'X'

    while True:
        for rotate in delta:
            ylooking, xlooking = yloc+rotate[0], xloc+rotate[1]
            
            if 0 <= ylooking < len(matrix) and 0 <= xlooking < len(matrix[0]) \
            and matrix[yloc+rotate[0]][xloc+rotate[1]] in currentcolor:
                
                stack.append([ylooking,xlooking])
                matrix[ylooking][xlooking] = 'X'
                
        if len(stack) == 0:
            break
        [yloc,xloc] = stack.pop()

col = int(input())
matrix = []
for i in range(col):
    matrix.append(list(input()))
matrix_blind = [[j for j in i] for i in matrix]

area_notblind, area_blind = 0,0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != 'X':
            DFS_visitcnt(matrix,i,j,False)
            area_notblind += 1
        if matrix_blind[i][j] != 'X':
            DFS_visitcnt(matrix_blind,i,j,True)
            area_blind += 1

print(f'{area_notblind} {area_blind}')
