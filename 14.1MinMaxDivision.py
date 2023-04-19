#binary search 的概念，和的最小為都切成一塊即串列中的最大值，和的最大為指切成一塊即串列總和


def get_blocks(K, A, Mid):

    blocks = 0
    temp_sum = 0
    for digit in A:
        temp_sum += digit

        if temp_sum > Mid:
            blocks +=1
            temp_sum = digit
    
    if A:
        blocks = blocks +1
    else:
        blocks
    #因為可能會有空串列
    return max(K,blocks)

def solution(K, M, A):
    
    if K == 1:
        return sum(A)
    
    upper = sum(A)
    lower = max(A)
    result = -1

    while upper >= lower:

        mid = (upper+lower)//2

        blocks = get_blocks(K,A,mid)

        if blocks > K:
            lower = mid +1
        ### if blocks <= K means I might find a minimal cadicate
        ### cuz = means fit K, and < meas I'vd use all the number can add no matter how many empty [] to fit K
        ### check if there is any lower value by update upper
        else:
            
            if result == -1:
                result = mid
            else:
                result = min(result, mid)
            upper = mid-1
    
    return result
