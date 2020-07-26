def quickSort2(arr):
    if len(arr) > 1:
        pivot = arr[0]

        equal = [i for i in arr if i == pivot]
        left = [i for i in arr if i < pivot]
        right = [i for i in arr if i > pivot]

        left = quickSort2(left)
        right = quickSort2(right)

        arr =  left + equal + right
    return arr

def quickSort(arr, start, end):
    if start <= end:
        pivot = arr[start]
        left = start
        right = end

        while left <= right:
            if arr[left] > pivot:
                if arr[right] < pivot:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        arr[right], arr[start] = arr[start], arr[right]
        quickSort(arr, start, right-1)
        quickSort(arr, right+1, end)

    return arr
