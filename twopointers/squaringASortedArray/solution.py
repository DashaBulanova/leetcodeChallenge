class Solution:
    def make_squares(self, arr):
        result = [0] * len(arr)

        pointer_1 = 0
        pointer_2 = len(arr) - 1

        insert_index = len(arr)-1
        while insert_index >= 0:
            left_square = pow(arr[pointer_1], 2)
            rigth_square = pow(arr[pointer_2], 2)
            result[insert_index] = max(left_square, rigth_square)

            if left_square > rigth_square:
                pointer_1 += 1
            else:
                pointer_2 -= 1

            insert_index -= 1

        return result
