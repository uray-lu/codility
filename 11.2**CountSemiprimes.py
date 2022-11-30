def solution(N, P, Q):
    
    #先找出小於N的串列中，誰是質數
    prime = [1]*(N+1)
    prime[0] = prime[1] =0
    for i in range(2, int(N**0.5)+1):
        if prime[i]:
            k = i*i

            while k<= N:
                prime[k] =0
                k+=i
    
    #再找出小於N的串列中，誰是semiprime
    semiprime = [0]*(N+1)
    semiprime[0] = semiprime[1] =0
    for i in range(N+1):
        for j in range(N+1):

            if prime[i] and prime[j] and i*j<=N:
                semiprime[i*j] = 1
            if i*j > N:
                break
    
    
    result = [0]*len(P)
    semiprimeCumsum = [0]*(N+1)
    s = 0
    #累加semiprime，方便check point的計算
    for i in range(N+1):
        if semiprime[i] == 1:
            s+=1
        semiprimeCumsum[i] = s
    
    
    for i in range(len(P)):

       result[i] = semiprimeCumsum[Q[i]] - semiprimeCumsum[P[i]-1]
    
    return result
