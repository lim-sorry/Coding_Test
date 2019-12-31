from math import floor

def solution(s):
    if len(s) % 2 == 1:
        answer = s[floor(len(s)/2)]
    else:
        answer = s[int(len(s)/2-1):int(len(s)/2+1)]
    return answer