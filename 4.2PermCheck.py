def solution(A):
    
    check = list(range(1,len(A)+1))
   
    if sorted(A) == check:
        return 1
    else:
        return 0
