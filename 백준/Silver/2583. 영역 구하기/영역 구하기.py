matrix = list(map(int,input().split(" ")))

rectangle = []
for i in range(matrix[2]):
    rectangle.append(list(map(int,input().split(" "))))
paper = [[0]*(matrix[1]) for i in range(matrix[0])]
for i in range(matrix[0]): #행 수
    for j in range(matrix[1]): #열 수
        for k in range(len(rectangle)): #rectangle 범위 안은 1로
            if j>=rectangle[k][0] and i>=rectangle[k][1] and j<rectangle[k][2] and i<rectangle[k][3]:
                paper[i][j] = 1

#dfs

def countarea(paper,starty,startx): #초기 starty, startx 주소 값이 0인 조건이 앞서 필요.
    delta = [[0,1],[1,0],[0,-1],[-1,0]] #방향 배열
    stack = [] #방문경로 저장 스택
    paper[starty][startx] = 1
    visitcount = 1
    while True:
        for lookaround in delta:
            if 0<=starty+lookaround[0]<=matrix[0]-1 and 0<=startx+lookaround[1]<=matrix[1]-1\
            and paper[starty+lookaround[0]][startx+lookaround[1]] == 0: #범위 내 0인 값 찾으면
                stack.append([starty+lookaround[0],startx+lookaround[1]]) #스택에 해당 주소 저장
                paper[starty+lookaround[0]][startx+lookaround[1]] = 1 
        if len(stack) == 0: #범위 내 0인 값 못 찾아서 남은 스택이 0인 경우
            break
        [starty,startx] = stack.pop() #스택의 마지막 주소에 있는 곳으로 좌표를 옮김   
        #paper[starty][startx]=1 ->문제점:스택에 있는 후보군은 계속 0으로 있으므로, 나중에 다른 곳에서 스택의 후보군을 중복해서 탐색해 새로 append하기 때문.             
        visitcount+=1
    return visitcount

answerlist = []
for i in range(matrix[0]): #행 수
    for j in range(matrix[1]): #열 수
        if paper[i][j] == 0:
            answerlist.append(countarea(paper,i,j))
print(len(answerlist))
answerlist.sort()
for i in answerlist:
    print(i,end = " ")