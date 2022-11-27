def solution(A):

    if len(A) == 0 or len(A) == 1:
        return 0
    
    current_profit = 0
    max_net_profit=0
    current_min = A[0]
    
    
    for i in range(1,len(A)):
        
        if A[i] < current_min:
            current_min = A[i]
            current_profit = 0
        else:
            current_profit += A[i]-A[i-1]
        
        if current_profit > max_net_profit:
            max_net_profit = current_profit
        
    
    return max_net_profit
