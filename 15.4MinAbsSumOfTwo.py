



def solution(A):
    
    if len(A) == 1:
        return 2*abs(A.pop())

    A.sort()
    front = 0
    back = len(A) -1
    
    #初始化最大的和絕對值以利找最小
    result = max(abs(A[-1]+A[-2]), abs(2*A[-1]), abs(A[0]+A[1]), abs(2*A[0]))
    
    #排序後，若前面的絕對值比後面大，代表是一個很大的負數配很小的正數，因此需往後找更小的負數，反之
    while front <= back:

        result = min(result, abs(A[front]+A[back]))

        if abs(A[front]) > abs(A[back]):
            front += 1
        else: 
            back -= 1

        if result == 0:
            return 0
    
    return result
