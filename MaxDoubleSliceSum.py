def solution(A):
    

    if len(A)<3:
        return 0
    
    prefix_left = [0]*(len(A))
    prefix_right = [0]*(len(A))

    s = 0
    for i in range(1, len(A)-1):
        
        s += A[i]

        if s<0:
            s=0
        prefix_left[i] = s

    s = 0 
    for i in range(len(A)-2, 0, -1):

        s += A[i]

        if s<0:
            s = 0
        prefix_right[i] = s  

    max_ = 0

    for i in range(0, len(A)-2):
        max_ = max(max_, prefix_left[i]+prefix_right[i+2])

    return max_        
