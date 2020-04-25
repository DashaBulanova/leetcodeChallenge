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
        backspace, i = 0, current_index - 1

        while i >= 0 and (origin[i] == '#' or backspace):
            backspace += 1 if origin[i] == '#' else -1
            i -= 1

        return i
