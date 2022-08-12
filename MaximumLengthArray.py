def solution(X, y):
    values = X.split()
    lengthremaining = y
    print(values)
    x = -1
    array_elements = []
    for val in values:
        x += 1
        if x > 0:
            lengthremaining -= 1

        if len(val) <= lengthremaining:
            array_elements.append(val)
            lengthremaining -= len(val)

    return ' '.join(array_elements)


print(solution('To crop or not to crop', 21))
