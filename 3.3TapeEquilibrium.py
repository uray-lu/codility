def solution(A):
    
    left_sum = 0
    right_sum = sum(A)
    result = []
    
    for i in range(len(A)-1):
        left_sum += A[i]
        right_sum -= A[i]

        result.append(abs(left_sum-right_sum))
    
    return min(result)
