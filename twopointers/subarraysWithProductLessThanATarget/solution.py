def find_subarrays(arr, target):
    start = 0
    acc = 1
    result = []

    for end in range(len(arr)):
        if arr[end] < target:
            acc *= arr[end]
            while acc >= target:
                acc /= arr[start]
                start += 1

            for i in range(start, end+1):
                result.append(arr[i:end+1])
        else:
            start = end + 1
            acc = 1

    return result

