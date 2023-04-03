class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        n = len(spells)
        result = [0] * n

        potions.sort()
        for i in range(n):
            result[i] = self.__search(spells[i], potions, success, 0, len(potions) - 1)
        return result

    def __search(self, spell: int, potions: list[int], success: int, s: int, e: int) -> int:
        if s == e:
            if spell * potions[s] < success:
                if s == len(potions)-1:
                    return 0
                else:
                    return len(potions) - s - 1
            else:
                return len(potions) - s

        m = s + (e - s) // 2
        if spell * potions[m] < success:
            return self.__search(spell, potions, success, m + 1, e)
        else:
            return self.__search(spell, potions, success, s, m)


"""
1, [1,2,3,4,5], 7, 0, 4

m = 2
1*3 < 7
__search(3,4)
m=3+0=3
4 => __search(4,4)


"""
