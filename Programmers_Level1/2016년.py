def solution(a, b):
    monthList = [31,29,31,30,31,30,31,31,30,31,30,31]
    dayList = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    return dayList[(sum(monthList[:a-1]) + b)%7]