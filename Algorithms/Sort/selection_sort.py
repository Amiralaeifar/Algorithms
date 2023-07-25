def selection_sort(arr):
    size = len(arr)
    i = 0
    while i < size - 1:
        min = i
        j = i + 1
        while j < size :
            if arr[j] < arr[min]:
                min = j
            j += 1
        arr[min], arr[i] = arr[i], arr[min]
        i += 1
    return arr
    