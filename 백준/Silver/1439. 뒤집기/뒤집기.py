c=[2,0]
for i in input():
    if i!=c[0]:
        c[1]+=1
        c[0]=i
print(int(c[1]//2))