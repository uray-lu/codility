def fibN(N):
    
    fiblist = [0]*(N+1)
    
    fiblist[0] = 1
    fiblist[1] = 1
    for i in range(2,len(fiblist)):
        fiblist[i] = fiblist[i-1]+fiblist[i-2]
    return fiblist



def solution(A, B):

    result =[]
    fib = fibN(max(A))
    
    for i in range(len(A)):
        
        ways = fib[A[i]]
        expo = B[i]

        result.append(ways%(2**expo))
    

    return result
  
  --------------------------------------------
  #學完位元運算跟二進位再看 這樣才100
  
  def solution(A, B):

    result =[]
    divisor = 2**max(B)
    
    fiblist = [0]*(max(A)+1)
    
    fiblist[0] = 1
    fiblist[1] = 1
    for i in range(2,len(fiblist)):
        fiblist[i] = (fiblist[i-1]+fiblist[i-2])
    
    for a,b in zip(A,B):
        #用二進制去比較不一樣的部分就是餘數
        result.append(fiblist[a] & 2**b-1)
    

    return result
