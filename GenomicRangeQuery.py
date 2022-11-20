def solution(S, P, Q):
    
    result = []
    query = {'A':1, 'C':2, 'G':3, 'T':4}

    for i in range(len(P)):
        for key in query.keys():
            if key  in S[P[i]:Q[i]+1]:
                min_ = query[key]
                break
        result.append(min_)
    
    return result
