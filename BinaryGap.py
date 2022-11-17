def solution(N):
    
    binary = bin(N)[2:]
    gap_list = binary.strip('0').split('1')
    len_list = []
    for element in gap_list:
        len_list.append(len(element))
    
    return max(len_list)
