
##因數成對，但完全平方數成對的有重複要

def solution(N):
    
    count = 0
    for i in range(1,int(N**0.5)+1):
        if N%i == 0:
            count+=1
    
    if N == int(N**0.5)*int(N**0.5):
        return count*2-1
    else:
        return count*2
