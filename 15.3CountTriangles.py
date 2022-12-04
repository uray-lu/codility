def solution(A):

    #  首先將A進行排序
    A.sort()
    count_triangle = 0
    for index, value in enumerate(A):
        middle_idx = index + 1
        biggest_idx = index + 2
        while biggest_idx < len(A):
            if value + A[middle_idx] > A[biggest_idx]:  # 此時可以構成三角形
                count_triangle += biggest_idx - middle_idx  # 最大值到中間值之間的均能構成三角形
                biggest_idx += 1  # 增大最大值
            elif middle_idx < biggest_idx - 1:  # 夠不成三角形，且最大值已經比中間值大超過1，代表需增加中間值，最大值不動
                middle_idx += 1
            else:  # 如果中間值沒有增加的餘地，則同時增加中間值和最大值。因爲只增加最大值，還是夠不成三角形
                biggest_idx += 1
                middle_idx += 1

    return count_triangle
