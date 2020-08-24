def binarySearch(arr,ele):
    pos = int(len(arr)/2)
    found = False

    while len(arr) != 0 and not found:
        if arr[pos]==ele:
            found = True
        else:
            if arr[pos] > ele:
                arr = arr[:pos]
                pos = int(pos/2)
            else:
                arr = arr[pos+1:]
                pos = int(pos/2)
    return found

def binarySearch2(arr,ele):
    first = 0
    last = len(arr)-1
    found = False

    while first <= last and not found:
        mid = int((first+last)/2)
        if arr[mid]==ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid-1
            else:
                first = mid+1
    return found

arr = [1,2,3,4,5,6,7,8,9,10,12,15,17,19,30,34,56, 110]
ele = 56

print(binarySearch2(arr,ele))
