def solution(A):
    
    sort = sorted(A)

    if len(A) == 1:
        return A.pop()
    
    for i in range(0, len(sort)-3, 2):
        if sort[i] != sort[i+1]:
            return sort[i]
    
    return sort.pop()
