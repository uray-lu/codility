def solution(N):
    
    factor = []
    for i in range(1,int(N**0.5)+1):
        if N%i == 0:
            factor.append(i)
    
    min_perimeter = int(2*(factor[0]+(N/factor[0])))

    for element in factor:
        perimeter = int(2*(element+(N/element)))
        
        min_perimeter = min(min_perimeter, perimeter)
    
    return min_perimeter
