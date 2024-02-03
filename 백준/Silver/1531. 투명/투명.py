matrix = [[0]*100 for i in range(100)]
N,M = map(int,input().split(" "))

nlist = []
for i in range(N):
    nlist.append(list(map(int,input().split(" "))))
for i in range(100):
    for j in range(100):
        for n in range(N):
            if j>=nlist[n][0]-1 and i>=nlist[n][1]-1 and j<=nlist[n][2]-1 and i<=nlist[n][3]-1:
                matrix[i][j] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j]>M:
            cnt+=1
print(cnt)