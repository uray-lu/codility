def solution(A):
    
    
    pivot = int(len(A)/2)
    check = {}
    leader = 0
    equi = 0
    for i in range(len(A)):
        check[str(A[i])] = 0
    
    for element in A:
        old_value = check[str(element)]
        new_value = old_value+1
        check[str(element)] = new_value
    
    for key in list(check.keys()):
        if check[key] > pivot:
            leader = int(key)
    
    prefix = [0]*len(A)
    for i in range(len(A)):
        if A[i] == leader:
            prefix[i] = prefix[i-1]+1
        else:
            prefix[i] = prefix[i-1]
    
    leader_count1= 0
    leader_count2= 0
    for i in range(len(A)-1):
        leader_count1 = prefix[i]
        leader_count2 = prefix[-1] - prefix[i]

        if leader_count1 > int((i+1)/2) and leader_count2 > int((len(A)-i-1)/2):
            equi += 1

    return equi
