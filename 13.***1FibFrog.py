def fib(n):
    
    if n >1:
        return (fib(n-1)+fib(n-2))
    return n


def solution(A):
    
    #include the bank from -1
    A.append(1)
    
    fib_list = []
    step = [0] * len(A)
    
    i = 2 #previous are 0 and 1 we don't need
    while fib(i) <= len(A):
        fib_list.append(fib(i))
        i+=1
    
    # check if there is a first step can achieve

    for i in fib_list:
        if A[i-1] == 1:
            step[i-1] = 1

    #search leaf more than one step

    for i in range(len(A)):
        if A[i] == 0 or step[i] > 0:
            continue
        
        min_index = -1
        min_value = 100000
        for j in fib_list:
            previous_index = i - j
            if previous_index <0:
                break
            if step[previous_index] > 0 and min_value > step[previous_index]:
                min_value = step[previous_index]
                min_index = previous_index
            
            if min_index != -1:
                step[i] = min_value +1
        
    if step[-1] > 0:
        return step[-1]
    else:
        return -1 
