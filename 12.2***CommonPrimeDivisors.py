#https://www.youtube.com/watch?v=F_th-1Rza_s

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)


def solution(A, B):
    
    count = 0

    for i in range(len(A)):
        a = A[i]
        b = B[i]
        D = gcd(a,b)
        while gcd(a,D) !=1:
            a /= gcd(a,D)
        while gcd(b,D) !=1:
            b /= gcd(b,D)
        
        if a==1 and b==1:
            count +=1
        
    
    return count
