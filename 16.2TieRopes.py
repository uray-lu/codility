def solution(K, A):
    
    count = 0
    rope = 0
    
    for element in A:
        
        
        if element < K:
            rope += element

            if rope >= K:
                count += 1
                rope =0
        else:
            count += 1
            rope = 0
    
    return count
