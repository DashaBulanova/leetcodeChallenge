class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = len(S)
        t = len(T)

        while s >= 0 and t >= 0:

            s = self.get_next_significant_index(S, s)
            t = self.get_next_significant_index(T, t)

            if (s >= 0) and (t >= 0) and T[t] != S[s]:
                return False
            elif (s >= 0) ^ (t >= 0):
                return False

        return True

    def get_next_significant_index(self, origin: str, current_index: int) -> int:
        if current_index == 0:
            return -1

        backspace = 0

        for i in range(current_index-1, -1, -1):
            if origin[i] == '#':
                backspace += 1
            elif backspace > 0:
                backspace -= 1
            else:
                return i

        return -1
