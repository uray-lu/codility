
#我只要判斷當前的線段起點有沒有比前面的終點大，若有則計算且更新終點，若無，直接判斷下一條線段即可


def solution(A, B):
    
    if len(A)== 0:
        return 0

    end = B[0]
    count = 1
    
    for i in range(1,len(A)):

        if A[i] > end:
            count +=1
            end = B[i]
        else:
            continue
    
    return count
