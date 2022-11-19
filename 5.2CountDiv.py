def solution(A, B, K):
    
    divisible = B//K - A//K

    if A%K == 0:
        divisible = divisible +1
    
    return divisible
