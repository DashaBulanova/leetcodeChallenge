def find_subarrays(arr, target):
    start = 0
    result = []
    acc = 1

    for end in range(len(arr)):
        acc = acc * arr[end]
        if arr[end] < target:
            result.append([arr[end]])
        if acc < target:
            if start != end:
                result.append(arr[start:end+1])
        else:
            while acc >= target:
                acc = acc / arr[start]
                start += 1

            if start != end:
                result.append(arr[start:end + 1])

    start += 1
    while start < len(arr)-1:
        acc = acc / arr[start]
        result.append(arr[start:len(arr)])
        start += 1

    return result

