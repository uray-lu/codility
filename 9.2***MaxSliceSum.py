### KADANE's Algorithm 

def solution(A):
    
    if len(A) == 1:
        return A.pop()
    
    total_max = A[0]
    current_max = A[0]
    
    for i in range(1, len(A)):

        if current_max+A[i] > A[i]:
            current_max += A[i]
        else:
            current_max = A[i] 
            
        if current_max > total_max:
            total_max = current_max
            
    return total_max

