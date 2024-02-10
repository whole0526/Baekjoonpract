def command(queue,input):
    global indexnum
    if input.startswith('push'):
        queue.append(int(input.split(' ')[1]))
    elif input == 'pop':
        try:
            print(queue[indexnum])
            indexnum += 1
        except:
            print(-1)        
    elif input == 'size':
        print(len(queue)-indexnum)
    elif input == 'empty':
        print(1 if len(queue)-indexnum == 0 else 0)
    elif input == 'front':
        try:
            print(queue[indexnum])
        except:
            print(-1)
    elif input == 'back':
        if len(queue)-indexnum == 0:
            print(-1)
        else:
            print(queue[-1])
    return queue
import sys
input = sys.stdin.readline
commandnum = int(input())
queue = []
indexnum = 0
for i in range(commandnum):
    queue = command(queue,input().rstrip())
