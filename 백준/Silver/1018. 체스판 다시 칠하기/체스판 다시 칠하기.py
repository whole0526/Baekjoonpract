col,row = map(int,input().split(' '))
matrix = []
for i in range(col):
    matrix.append(input())
incorrectlist = []
for i in range(col-7):
    for j in range(row-7):
        incorrect = 0
        for k in range(8):
            for l in range(8):
                if ((k+i+l+j)%2 == 0 and matrix[k+i][l+j] == 'B') or ((k+i+l+j)%2 == 1 and matrix[k+i][l+j] == 'W'):
                    continue
                else:
                    incorrect += 1
        
        incorrectlist.append(incorrect)
        incorrectlist.append(64-incorrect)
print(min(incorrectlist))