def solution(A, K):
    while K > 0:
        A = rotate(A)
        K -= 1
    return A


def rotate(A):
    count = 0
    shifted_array = []
    for val in A:
        count += 1
        if count < len(A):
            print(count)
            shifted_array.insert(count, val)
        else:
            shifted_array.insert(0, val)
    return shifted_array


print(solution([2, 3, 4, 5, 6], 2))
