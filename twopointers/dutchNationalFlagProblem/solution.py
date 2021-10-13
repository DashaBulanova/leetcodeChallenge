def dutch_flag_sort(nums):
    next_null_pos = 0
    next_two_pos = len(nums) - 1
    pointer = 0

    while pointer <= next_two_pos:
        if nums[pointer] == 0:
            nums[pointer], nums[next_null_pos] = nums[next_null_pos], nums[pointer]
            next_null_pos += 1
            pointer += 1
        elif nums[pointer] == 2:
            nums[pointer], nums[next_two_pos] = nums[next_two_pos], nums[pointer]
            next_two_pos -= 1
        else:
            pointer += 1

    return
