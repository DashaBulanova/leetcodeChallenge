def find_max(arr)-> int:
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = start + int((end - start)/2)
        if arr[mid]<arr[mid+1]:
            start = mid+1
        else:
            end = mid

    return arr[start]