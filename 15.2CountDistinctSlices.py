def solution(M, A):
    
    list_len = len(A)
    result, front, back = 0 ,0, 0
    visited = [False]*(M+1)


    while back < list_len :

        if front < list_len and visited[A[front]] == False:
            #每增加一個數字多這麼多slice組合
            result += front - back +1
            visited[A[front]] = True
            front +=1
        
        else:
            visited[A[back]] = False
            back += 1
        
        if result > 1000000000:
            return 1000000000
    return result
