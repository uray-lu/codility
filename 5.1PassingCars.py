def solution(A):
    
    
    if len(A) == 1:
        return 0
    if len(A) == sum(A):
        return 0
    if sum(A) == 0:
        return 0
    
    total_pair = 0
    max_pair = sum(A)
    for element in A:
        if element == 1:
            max_pair -= 1
        else:
            total_pair += max_pair

    if total_pair > 1000000000:
        return -1  
    
    return total_pair
