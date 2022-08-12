def solution(A):
    data_list=[]
    while A:
        minimum = A[0]
        for X in A:
            if X<minimum:
                minimum=X
        data_list.append(minimum)
        A.remove(minimum)

    print(data_list)

solution([4, 1, 2, -4, -3, -3])
