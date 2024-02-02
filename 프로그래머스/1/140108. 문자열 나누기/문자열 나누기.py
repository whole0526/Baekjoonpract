def solution(s):
    temp = ''
    splitword = []
    countchar = {'firstchar':0,'notfirstchar':0}
    for char in s:
        temp += char
        if temp[-1] != temp[0]:
            countchar['notfirstchar'] +=1
        else:
            countchar['firstchar'] +=1
        if countchar['firstchar'] == countchar['notfirstchar']:
            splitword.append(temp)
            temp = ''            
            countchar['firstchar'], countchar['notfirstchar'] = 0,0
    if len(temp)>0:
        splitword.append(temp)
    return len(splitword)