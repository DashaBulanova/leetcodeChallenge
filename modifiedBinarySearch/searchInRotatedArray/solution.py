
def search_rotated_array(arr, key):
    if len(arr) == 0:
        return -1
    start = 0
    end = len(arr)-1
    while start<end:
        mid = start + (end-start)//2
        if arr[mid]==key:
            return mid

        if arr[start]<=arr[mid]: #started part is sorted
            if arr[start] <= key < arr[mid]:
                end = mid
            else:
                start = mid+1
        else: # end part is sorted arr[mid]<arr[end]
            if  arr[mid] < key <= arr[end]:
                start = mid + 1
            else:
                end = mid
    return start if arr[start]==key else -1
