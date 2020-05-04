class Solution(object):
    def bitwiseComplement(self, num: int) -> int:
        result = ''
        for c in str(bin(num)).replace('0b', ''):
            result += '0' if c == '1' else '1'
        return int(result, 2)
