def solution(A):
    
    sort = sorted(A)

    pro1 = int(sort[0]*sort[1]*sort[-1])
    pro2 = int(sort[-1]*sort[-2]*sort[-3])

    if 0 in A:
        return max(0, pro1, pro2)
    else:
        return max(pro1, pro2)
