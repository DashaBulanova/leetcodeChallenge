from typing import List

def find(input, target, start, end)-> List[int]:
    if start > end:
        return [-1,-1]
    if start == end:
        return [start, end] if input[start] == target else [-1,-1]

    mid = start + int((end-start)/2)
    mid_item = input[mid]
    if mid_item == target:
        right = find(input, target, mid+1, end)
        left = find(input, target, start, mid-1)

        if left == [-1, -1] and right == [-1,-1]:
            return [mid, mid]
        if left == [-1, -1]:
            return [mid, right[1]]
        if right == [-1, -1]:
            return [left[0], mid]
        return [left[0], right[1]]
    
    elif mid_item > target:
        return find(input, target, start, mid-1)
    else:
        return find(input, target, mid+1, end)

def find_key_range(input: List[int], target: int) -> List[int]:
    return find(input, target, 0, len(input)-1)