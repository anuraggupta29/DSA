def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                c = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = c
    return arr
