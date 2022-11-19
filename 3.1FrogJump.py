def solution(X, Y, D):
    
    if (Y-X)%D != 0:

        return int(((Y-X)//D)+1)
    
    else:
        return int((Y-X)/D)
