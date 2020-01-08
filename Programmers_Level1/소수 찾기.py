def solution(n):
    alist=[True] * n
    alist[0]=False
    for i, stat in enumerate(alist):
        if stat is True:
            j=2
            while (i+1)*j<=n:
                alist[(i+1)*j-1]=False
                j+=1
    return alist.count(True)