def solution(A):
    
    
    for i in range(len(A)):
        A[i] = abs(A[i])
    M = max(A)
    S = sum(A)
    count = [0]* (M+1)

    for element in A:
        count[element] +=1
    
    dp = [-1]*(S+1)
    dp[0] = 0

    for a in range(1, M+1):
        if count[a] > 0:
            for b in range(S):
                if dp[b] >= 0:
                    dp[b] = count[a]
                elif b >= a and dp[b-a] > 0:
                    dp[b] = dp[b-a]-1
    
    result = S
    for i in range(S//2+1):
        if dp[i] >= 0:
            #扣掉累加到最接近一半的總和
            result = min(result, S-2*i)
    return result
