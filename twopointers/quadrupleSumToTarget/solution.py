from typing import List


def search_pair(arr, target, i, x1, x2) -> List[List[int]]:
    res = []
    left, right = i + 1, len(arr) - 1
    while left < right:  # O(N)
        if arr[left] + arr[right] == target:
            res.append([x1, x2, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1

    return res


def search_triplet(arr, target, i, x1) -> List[List[int]]:
    res = []
    prev = None
    for j in range(i + 1, len(arr) - 2):  # O(N-2)
        if arr[j] == prev:
            continue
        r = search_pair(arr, target - arr[j], j, x1, arr[j])
        if r:
            res.extend(r)
        prev = arr[j]
    return res


def search_quadruplets(arr, target):
    quadruplets = []
    prev = None
    sorted_arr = sorted(arr)  # O(NlogN)
    for i in range(len(sorted_arr) - 3):  # O(N-4)*O(N-2)*O(N) => O(n^3)
        if sorted_arr[i] == prev:
            continue
        res = search_triplet(sorted_arr, target - sorted_arr[i], i, sorted_arr[i])
        if res:
            quadruplets.extend(res)
        prev = sorted_arr[i]
    return quadruplets
