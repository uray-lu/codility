def solution(S, P, Q):
    result = []
    A = [0]*len(S)
    C = [0]*len(S)
    G = [0]*len(S)
    T = [0]*len(S)

    a = c = g = t = 0

    for i in range(len(S)):
        if S[i] == 'A':
            a += 1
        elif S[i] == 'C':
            c += 1
        elif S[i] == 'G':
            g += 1
        elif S[i] == 'T':
            t += 1
        A[i] = a
        C[i] = c
        G[i] = g
        T[i] = t
    
    for j in range(len(P)):

        if P[j] == Q[j]:
            if S[P[j]] == 'A':
                result.append(1)
            elif S[P[j]] == 'C':
                result.append(2)
            elif S[P[j]] == 'G':
                result.append(3)
            elif S[P[j]] == 'T':
                result.append(4)
    
        else:
            if A[P[j]]< A[Q[j]] or S[P[j]] == 'A':
                result.append(1)
            elif C[P[j]]< C[Q[j]] or S[P[j]] == 'C':
                result.append(2)
            elif G[P[j]]< G[Q[j]] or S[P[j]] == 'G':
                result.append(3)
            elif T[P[j]]< T[Q[j]] or S[P[j]] == 'T':
                result.append(4)

    return result
