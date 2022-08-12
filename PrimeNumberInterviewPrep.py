def ReverseList(N):
    primeNumbers = []
    for value in range(2, N):
        if all(value % f != 0 for f in range(2, value)):
            primeNumbers.append(value)
    return primeNumbers


print(ReverseList([1,3,2,4,5,3,4,6,6]))
