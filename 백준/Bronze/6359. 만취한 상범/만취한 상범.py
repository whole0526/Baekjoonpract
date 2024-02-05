def sol(roomnum):
    rooms = [0]*roomnum
    for i in range(1,roomnum+1):#배수
        j = i-1
        while j <=roomnum-1:
            rooms[j] = 1 if rooms[j] == 0 else 0
            j += i
    return rooms.count(1)

attempt = int(input())
roomnum = []
for i in range(attempt):
    roomnum.append(int(input()))
for i in range(attempt):
    print(sol(roomnum[i]))