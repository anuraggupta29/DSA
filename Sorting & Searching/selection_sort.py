def selectionSort(arr):
    for i in range(len(arr)):
        min = arr[i]
        minI = i
        for j in range(i+1,len(arr)):
            if arr[j]<min:
                min = arr[j]
                minI = j
        arr[minI] = arr[i]
        arr[i] = min

    return arr
