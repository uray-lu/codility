###從反面想，先算divsor有多少再用整個串列去扣掉divsor剩下就是nonedivisor數量


def solution(A):
    
    noneDiv = {}
    counts = [0]*(max(A)+1)
    
    #做一個array看裡面有多少個比最大值小的數，因為都可能是因數，且遍歷此array可以直接累加divisor數量
    for element in A:
        counts[element] += 1
    
    #重複的我就不重算了
    short = set(A)
    for element in short:
        div = 0
        for i in range(1,int(element**0.5)+1):
            if element % i == 0 :
                div += counts[i]
                #加進成對的因數且避免重複算完全平方數
                if int(element/i) != i:
                    div += counts[int(element/i)]
                
        noneDiv[element] = len(A) - div
    
    result = []
    for element in A:
        result.append(noneDiv[element])
    
    return result
