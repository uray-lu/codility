def solution(A):
    

    
    peak = []
    for i in range(1,len(A)-1):

        if A[i-1]<A[i] and A[i]>A[i+1]:
            peak.append(i)
        
    if len(peak) == 0:
        return 0
    
    for k in range(len(peak), 0 , -1):
        if len(A)%k != 0:
            continue
        
        LenEachSlice = int(len(A)/k)
        slices = [0]*k
        
        #無條件捨去的商就會是落在分段完成後的第幾段
        for p in peak:
            slice_id = p//LenEachSlice
            if slices[slice_id] == 0:
                slices[slice_id] =1
        
        if sum(slices) == k:
            return k
    return 0
    
