def swap(a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


def selection_sort(array, n):
    for i in range(n):
        mindex = i
        for k in range(i + 1, n):
            if array[k] < array[mindex]:
                mindex = k
        swap(i, mindex)

array = [3, 6, 9, -8, 1]
selection_sort(array, len(array))
print array
