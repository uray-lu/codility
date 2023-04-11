

# think reversly !!!

def solution(A):
    
    max_pair = sum(A)
    total_pair = 0

    for car in (A):
        if car == 1:
            max_pair -= 1
        else:
            total_pair += max_pair
    
    if total_pair > 1000000000:
        return -1
    
    return total_pair
