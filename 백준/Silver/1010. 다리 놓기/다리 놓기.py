import math
for i in range(int(input())):
    n,m = map(int,input().split())
    print(math.comb(m,n))