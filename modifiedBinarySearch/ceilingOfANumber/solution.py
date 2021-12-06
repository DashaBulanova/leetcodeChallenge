import math

def find_ceiling(input, target, i, j)->int:
    if i == j:
        return i if input[i]>=target else -1

    mid = i + int((j-i)/2)
    mid_item = input[mid]
    if mid_item == target:
        return mid

    if mid_item > target:
        left = find_ceiling(input, target, i, mid)
        if left == -1:
            return mid
        else:
            return min(mid, left)
    return find_ceiling(input, target, mid+1, j)

def ceiling(input, target) -> int:
    return find_ceiling(input, target, 0, len(input)-1)


