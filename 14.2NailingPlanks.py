BEGIN_POS = 0
END_POS = 1
NAIL_COUNT_ADDRESS = 0
HIT_POS = 1

def binary_search_nail_pos(nails, plank):
    beg = 0
    end = len(nails) - 1
    ptr = -1

    while beg <= end:
        mid = (beg + end) // 2

        if nails[mid][HIT_POS] < plank[BEGIN_POS]:
            beg = mid + 1
        elif nails[mid][HIT_POS] > plank[END_POS]:
            end = mid - 1
        #當這片木板可以被釘上去，就保留這個mid但這個mid不一定是最小的釘子序，故我還要找找看有沒有更小的
        else:
            end = mid - 1
            ptr = mid

    return ptr

def solution(A, B, C):

    count = 0
    planks = zip(A, B)
    nails = sorted(enumerate(C), key =  lambda var: var [HIT_POS])

    for plank in planks:
        nail_pos =  binary_search_nail_pos(nails, plank)

        if nail_pos == -1:
            return -1

        nail_count = nails[nail_pos][NAIL_COUNT_ADDRESS]
        
        #我先確認這個點比總釘子數小，且位置小於此木板的結尾，因為二元搜尋的關係，找到的釘子位置一定已經大於木板的頭
        while nail_pos < len(nails) and nails[nail_pos][HIT_POS] <= plank[END_POS]:
            nail_count = min(nail_count, nails[nail_pos][NAIL_COUNT_ADDRESS])
            
            #當我發現此數量小於之前的計算過的數量，代表這個木板一定可以被這根釘子釘上去故break
            if nail_count <= count:
                break
            
            nail_pos += 1
        #更新數量，如果有更後面的釘子才更新
        count = max(count, nail_count)

    return count + 1
