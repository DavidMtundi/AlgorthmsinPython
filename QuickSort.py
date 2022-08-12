def QS(arr, left, right):
    return QuickSort(arr, left, right)


def QuickSort(arr, left, right):
    if left >= right:
        return arr
    p = Partitition(arr, left, right)

    QS(arr, left, p - 1)
    QS(arr, p + 1, right)
    return arr


def Partitition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if pivot > arr[j]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1;


arrayprovided = [-1, -2, 9, 0, 3, -4, 5, 6, 1, 0, -1]
anotherarray = [0, 1, 2, 3, 9, 8, 7, 4, 2, -10, 3, -20, 9, 0]
print(QS(arrayprovided, 0, len(arrayprovided) - 1))
print(QS(anotherarray, 0, len(anotherarray) - 1))
