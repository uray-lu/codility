def solution(A):
    A.sort()
    min = 1
    for elem in A:
        if elem == min:
            min+=1
    return min
