def solution(A):
    
    if len(A) <3:
        return 0
    
    sort = sorted(A)
    
    for i in range(len(A)-2):

        if sort[i]+sort[i+1] > sort[i+2]:
            return 1

    return 0
