def solution(n, lost, reserve):
    answer = n
    for i in lost:
        if i in reserve:
            reserve.pop(reserve.index(i))
            lost.pop(lost.index(i))
    for i in lost:
        count=0
        for j in [-1,1]:
            if (i+j) in reserve:
                count+=1
        lost[lost.index(i)]=[i,count]
    lost.sort(key=lambda x: x[1])
    for i in lost:
        for j in [1,-1]:
            if (i[0]+j) in reserve:
                reserve.pop(reserve.index(i[0]+j))
                i[0]=0
                break
    for i in lost:
        if i[0] != 0:
            answer -= 1
    return answer