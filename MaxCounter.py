def solution(N, A):
    counter = [0]*N
    base = 0
    max_counter = 0
    for element in A:
        if element>=1 and element<=N:
            counter[element -1] = max(base, counter[element -1])+1
            max_counter = max(counter)
        elif element == N+1:
            base = max_counter
    
    for i in range(N):
        counter[i] = max(base, counter[i])

    
    return counter
