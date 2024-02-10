def josephus(n,k):
    nlist = [i+1 for i in range(n)]
    dequeindex = 0
    removelist = []
    while dequeindex < len(nlist):
        if (dequeindex+1)%k == 0:
            removelist.append(nlist[dequeindex])
        else:
            nlist.append(nlist[dequeindex])
        dequeindex += 1
    return removelist

n,k = map(int,input().split(' '))
temp = '<'+', '.join(list(map(str,josephus(n,k))))+'>'
print(temp)