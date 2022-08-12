def solution(A):
    # convert the value to a string
    charval = []
    valuesfirst = getbinary(A, charval)
    values = ''.join([str(elem) for elem in valuesfirst])
    if values.__contains__('1'):
        if values.rindex('1') < len(values) - 1:
            values = values[:values.rindex('1') + 1 - len(values)]
    array_values = values.split('1')
    maxlength = 0
    for val in array_values:
        if len(val) > maxlength:
            maxlength = len(val)
    return maxlength


def getbinary(N, charval):
    if N < 1:
        return charval
    if N // 2 != 0:
        charval.insert(0, str((N % 2)))
        N = N // 2
        getbinary(N, charval)
    else:
        charval.insert(0, str(N))
    return charval


print(solution(9))
