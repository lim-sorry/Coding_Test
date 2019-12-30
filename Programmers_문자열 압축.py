from math import *

def solution(s):
    answer = len(s)
    for i in range(1,answer+1): #i = [0:len(s)]
        list2 = [['',0]]
        answer2 = 0
        for j in range(len(s)//i):
            a = ''
            for l in range(i):
                a += s[j*i+l]
            if list2[-1][0] == a:
                list2[-1][1] += 1
            else:
                list2.append([a,1])
        for k in list2:
            answer2 += len(k[0])
            if k[1] > 1:
                answer2 += floor(log10(k[1]))+1
        answer2 += len(s)%i
        answer = min(answer, answer2)
    return answer