def find_pair(arr, target, left_index):
    count = 0
    right_index = len(arr) - 1

    while left_index < right_index: #O(N)
        left = arr[left_index]
        right = arr[right_index]
        if left + right < target:
            count += right_index - left_index
            left_index += 1
        else:
            right_index -= 1

    return count


def triplet_with_smaller_sum(arr, target):
    count = 0
    sorted_arr = sorted(arr) #O(n*log(n))
    i = 0
    while i < len(arr) and sorted_arr[i] <= target: #O(N)
        count += find_pair(sorted_arr, target-sorted_arr[i], i + 1)
        i += 1
    return count

#Time complexity: O(n*log(n) + O(N^2))
#Space complexity: 0(N)

"""
sorted = [-1, 0, 2, 3], target = 3
init triplet_with_smaller_sum: i = 0

step 1: -1 <= 3 => true
    find_pair( [-1, 0, 2, 3], 3, -1, 1)
                right_index = 4-1= 3
         step 1:    while 1<3
                    left = arr[1] = 0
                    right = arr[3]=3
                    if -1 + 0 + 3 < 3 => 2 < 3 => True:
                        count = 1
                        right_index = 2
        step 2:    while 1 < 2 => true
                     left = 0
                     right = 2
                     if -1 +0 +2 < 3 => 1 < 3 => true:
                        count = 2
                        right_index = 1
                        
        step 3: while 1 < 1 False
        
        return 2
count = 2
i = 1
step 2: 0 < 3 => true
    find_pair( [-1, 0, 2, 3], 3, 0, 2)
        step 1: while 2 < 3 True
        left = 2
        right =3
        0+2+3 = 5 < 3 False:
        left_index =3 
        
        return 0
    0

"""
