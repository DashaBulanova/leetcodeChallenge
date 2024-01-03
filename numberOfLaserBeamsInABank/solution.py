class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        result = 0
        prev = 0
        for row in bank:
            curr = row.count('1')
            if curr != 0:
                result += curr * prev
                prev = curr
        return result
