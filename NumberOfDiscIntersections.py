def solution(A):
    if len(A) == 0 or len(A) == 1:
        return 0
        
         
    start = []
    end = []
    c_start =[0]*len(A)
    c_end =[0]*len(A)
    cc_start =[0]*len(A)
    cc_end =[0]*len(A)
    total = 0
    
    
    for i in range(len(A)):
        if i-A[i]<0:
            start.append(0)
        else:
            start.append(i-A[i])
        
        if i+A[i] > max(A):
            end.append(max(A))
        else:
            end.append(i+A[i])


    for element in start:
        c_start[element] += 1 
    
    for element in end:    
        c_end[element] += 1
    
    for k in range(len(c_start)):
        cc_start[k] = c_start[k]+cc_start[k-1]

    for k in range(len(c_end)):
        cc_end[k] = c_end[k]+cc_end[k-1]

    
    for i in range(len(A)):
        if i == 0:
            total += (cc_start[i] - c_start[i])*c_start[i] + (c_start[i]*(c_start[i]-1)/2)
        else:
            total += (cc_start[i] - cc_end[i-1] - c_start[i])*c_start[i]+ (c_start[i]*(c_start[i]-1)/2)

    if total > 10000000:
        return -1
    else:
        return int(total) 
