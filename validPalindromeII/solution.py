class Solution:
    def validPalindrome(self, s: str) -> bool:

        def validPalindrome(start, end, skipped):
            l = start
            r = end
            while l <= r:
                if s[l] == s[r]:
                    return validPalindrome(l + 1, r - 1, skipped)
                else:
                    if skipped >= 1:
                        return False
                    else:
                        skipped += 1
                        if validPalindrome(l + 1, r, skipped):
                            return True
                        elif validPalindrome(l, r - 1, skipped):
                            return True
                        else:
                            return False
            return True

        return validPalindrome(0, len(s) - 1, 0)
