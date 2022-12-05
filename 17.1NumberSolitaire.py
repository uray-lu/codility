def solution(A):
    
    path = [A[0]]

    for i in range(1,len(A)-1):

        if len(path) < 6:
            path.append(max(path)+A[i])
        else:
            path.append(max(path)+A[i])
            path.pop(0)

    
    return max(path)+A[-1]
