class Solution(object):
    bitsCount = []
    biggest_power = int

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        self.bitsCount = [None] * (num + 1)
        self.biggest_power = 0
        for i in range(0, num + 1):
            self.bitsCount[i] = self.get_bits_count(i)

        return self.bitsCount

    def get_bits_count(self, i):
        if i == 0:
            return 0
        remainder = (i % (2 ** self.biggest_power))

        if remainder == 0:
            if i != 1:
                self.biggest_power += 1
            return 1

        return 1 + self.bitsCount[remainder]
