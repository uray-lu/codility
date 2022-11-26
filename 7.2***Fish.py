def solution(A, B):
    
    down = []
    eaten = 0

    for i in range(len(B)):

        if B[i] == 1:
            down.append(A[i])
        else:
            while len(down) !=0:
                if down[-1] > A[i]:
                    eaten +=1
                    break
                elif down[-1] < A[i]:
                    down.pop()
                    eaten += 1
    
    return len(A) - eaten
