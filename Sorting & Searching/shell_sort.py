def shellSort(arr):

    gap = len(arr)//2

    while gap != 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i
            while j>=gap and arr[j]<arr[j-gap]:
                #temp = arr[j]
                arr[j] = arr[j-gap]
                #arr[j-gap] = temp
                j -= gap

            arr[j] = temp
        gap = gap//2

    return arr
