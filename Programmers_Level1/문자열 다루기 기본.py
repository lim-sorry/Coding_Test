def solution(s):
    if len(s) not in [4, 6]:
        answer = False
    else:
        answer = True
        for i in s:
            if i.isnumeric() == False:
                answer = False
                break
    return answer