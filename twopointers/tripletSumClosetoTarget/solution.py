def triplet_sum_close_to_target(arr, target_sum):
    sorted_arr = sorted(arr)
    result = None
    for i in range(len(sorted_arr) - 2):
        res = find_min_pair(target_sum, sorted_arr[i], i + 1, sorted_arr)
        if res == 0:
            return 0
        if result:
            result = min(res, result)
        else:
            result = res
    return result[1]

def find_min_pair(target, first_item, left_index, arr):
    right_index = len(arr) - 1
    result = None
    while left_index < right_index:
        left = arr[left_index]
        right = arr[right_index]

        if first_item + left + right == target:
            return 0, 0
        if first_item + left + right > target:
            right_index -= 1
        else:
            left_index += 1

        result = (min((abs(target - (first_item + right + left)), (first_item + right + left)), result)
                  if result
                  else (abs(target - (first_item + right + left)), (first_item + right + left)))

    return result
