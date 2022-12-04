def solution(A):
    
 

    for i in range(len(A)):
       if A[i] < 0 :
           A[i] = -A[i]
        
    a = set(A)

    return len(a)
