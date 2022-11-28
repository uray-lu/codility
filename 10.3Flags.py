def solution(A):
    if len(A) <3:
        return 0
    
    peak = []
    for i in range(1,len(A)-1):

        if A[i-1]<A[i] and A[i]>A[i+1]:
            peak.append(i)
    
    if len(peak) == 0:
        return 0
    elif len(peak) == 1:
        return 1

    count = 1
    max_flag =0
    
    for k in range(min(len(peak), int(len(A)**0.5))+1, 0, -1):
        
        lastflag = 0
        count = 1
        for i in range(1,len(peak)):
            if (peak[i] - peak[lastflag]) >= k and count<k:
                count +=1
                lastflag = i
        
        if count < max_flag:
            return max_flag
        elif count > max_flag:
            max_flag = count
