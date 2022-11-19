def solution(A):
    
    if len(A) == 0:
        return 1
    elif len(A) == 1:
        if A[0] == 1:
            return 2
        return 1
    else:
        n = len(A)+1
        sum_ = sum(A)
        return int((n*(n+1))/2 - sum_)
    
