def solution(A):
    result = 0
    initial_min = (A[0]+A[1])/2
    prefix_sum = [0]*(len(A)+1)
    
    for i in range(len(A)):
        prefix_sum[i+1] = A[i]+prefix_sum[i]
    
    for p in range(len(A)-1):
        for q in range(p+1,len(A)):
            
            current_value = (prefix_sum[q+1]-prefix_sum[p])/(q-p+1)

            if initial_min > current_value:
                initial_min = current_value
                result = p
            elif initial_min == current_value:
                result = min(result,p)
    
    return result
  
  
  _______________ optimal 只討論slice = 2 or 3 ______________________
  def solution(A):
    
    # write your code in Python 2.7
    N = len(A)

    index = 0
    max = (A[0] + A[1]) / 2.0
    for ind in range(N - 1):
        avg2 = (A[ind] + A[ind + 1]) / 2.0

        if avg2 < max:
            max = avg2
            index = ind

        if ind <= N - 3:
            avg3 = (A[ind] + A[ind + 1] + A[ind + 2]) / 3.0

            if avg3 < max:
                max = avg3
                index = ind

    return index
