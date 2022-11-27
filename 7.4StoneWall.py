def solution(H):
    

    topbase = [H[0]]
    total = 1

    for i in range(len(H)):
        if H[i] != topbase[-1]:
            while len(topbase) != 0:
                if H[i]  < topbase[-1]:
                    topbase.pop()
                    if len(topbase) == 0:
                        topbase.append(H[i])
                        total += 1
                        break
                    else:
                        pass
                        
                elif H[i] > topbase[-1]:
                    total += 1
                    topbase.append(H[i])
                    break
                elif H[i]  == topbase[-1]:
                    break           

    return total  
