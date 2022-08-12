def solution(P, S):
    # write your code in Python 3.6
    sumP = 0
    # find the total people
    for i in P:
        sumP += i

    if max(S) > sumP:
        return 1
    else:
        # sort S in desc order
        sorted_array = []
        while S:
            maximumvalue = 0
            for value in S:
                if value > maximumvalue:
                    maximumvalue = value
            sorted_array.append(maximumvalue)
            S.remove(maximumvalue)

        sum_values = 0
        count = 0
        for v in sorted_array:
            sum_values += v
            count += 1
            if sum_values >= sumP:
                return count


print(solution([2, 3, 4, 2], [2, 5, 7, 2]))
