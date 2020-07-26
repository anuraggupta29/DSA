def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i
        temp = arr[j]
        while j>0 and temp<arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp

    return arr
