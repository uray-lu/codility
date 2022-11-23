def solution(A):
    
    count_map = {}

    for element in A:
        count_map[str(element)] = 1
    
    distinct = list(count_map.keys())

    return len(distinct)
