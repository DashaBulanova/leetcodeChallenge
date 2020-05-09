from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        try:
            (a, b) = self.get_polynomial_constants(coordinates[0], coordinates[1])

            for i in range(2, len(coordinates)):
                x = coordinates[i][0]
                y = coordinates[i][1]

                if x * b + a != y:
                    return False
        except:
            x = coordinates[0][0]
            for i in range(1, len(coordinates)):
                if coordinates[i][0] != x:
                    return False

        return True

    def get_polynomial_constants(self, coordinates1: List[int], coordinates2: List[int]) -> (int, int, int):
        x1, y1 = coordinates1[0], coordinates1[1]
        x2, y2 = coordinates2[0], coordinates2[1]

        if x1 == x2:
            raise Exception

        a = y1 - x1 * ((y2 - y1) / (x2 - x1))
        b = (y2 - y1) / (x2 - x1)
        return a, b
