def solution(A):
    data_list = []
    while A:
        minimum = A[0]
        for X in A:
            if X < minimum:
                minimum = X
        data_list.append(minimum)
        A.remove(minimum)
    if data_list[0] > 1:
        return 1
    elif data_list[len(data_list) - 1] < 1:
        return 1
    else:
        for element in data_list:
            if element > 0:
                if element + 1 not in data_list:
                    return element + 1


print(solution([-1, -1, -4]))
