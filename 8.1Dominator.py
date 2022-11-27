def solution(A):
    
    if len(A) == 0:
        return -1

    pivot = int(len(A)/2)
    check = {}
    position = {}
    result = []
    
    for i in range(len(A)):
        check[str(A[i])] = 0
        position[str(A[i])] = i
    
    for element in A:
        old_value = check[str(element)]
        new_value = old_value+1
        check[str(element)] = new_value
    
    for key in list(check.keys()):
        if check[key] > pivot:
            result.append(position[key])

    if len(result) == 0:
        return -1
    else:
        return result[0]    
