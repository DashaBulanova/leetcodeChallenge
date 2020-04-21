import math


class Solution(object):
    def peak_index_in_mountain_array(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return self.lookup_peak(0, len(A) - 1, A)

    def lookup_peak(self, start_index, end_index, A):
        n = end_index - start_index

        if n <= 1:
            if A[start_index] > A[end_index]:
                return start_index
            else:
                return end_index

        else:
            middle_point = start_index+int(math.floor(n/2))

            if A[middle_point] < A[middle_point + 1]:
                return self.lookup_peak(middle_point + 1, end_index, A)

            if A[middle_point] < A[middle_point - 1]:
                return self.lookup_peak(start_index, middle_point - 1, A)

            return middle_point
