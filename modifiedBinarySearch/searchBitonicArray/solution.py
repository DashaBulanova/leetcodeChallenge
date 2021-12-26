def search_bitonic_array(arr, key):
    if len(arr) == 0:
        return -1

    def search(arr, key, start, end) -> int:
        if start == end or start > end:
            return start if arr[start] == key else -1

        mid = start + (end - start) // 2
        if key == arr[mid]:
            return mid
        left = search(arr, key, start, mid)
        right = search(arr, key, mid + 1, end)

        return left if left != -1 else right

    return search(arr, key, 0, len(arr) - 1)
