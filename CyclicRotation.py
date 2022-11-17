def solution(A, K):
    
    if len(A) == 0:
        return A
    
    for _ in range(K):
        A.insert(0, A.pop())
    return A
