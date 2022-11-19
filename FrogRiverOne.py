def solution(X, A):
    
    
    leaf = {}
    
    for i  in range(len(A)):
        leaf[str(A[i])] = i
        if len(leaf) == X:
            return i
    
    return -1
