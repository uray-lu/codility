#最大公因數跟最小公倍數的概念

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)




def solution(N, M):
    
    return int(N/gcd(N,M))
