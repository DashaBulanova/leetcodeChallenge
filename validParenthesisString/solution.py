class Solution:
    def checkValidString(self, s: str) -> bool:
        B, Z = [], []

        for i, c in enumerate(s):
            if c == '(':
                B.append(i)
            elif c == '*':
                Z.append(i)
            elif c == ')':
                if B:
                    B.pop()
                elif Z:
                    Z.pop()
                else:
                    return False

        if len(B) == 0:
            return True

        if len(B) > len(Z):
            return False

        for i in range(len(B) - 1, -1, -1):
            j = Z.pop()
            if j > B[i]:
                B.pop()
            else:
                return False

        return True
