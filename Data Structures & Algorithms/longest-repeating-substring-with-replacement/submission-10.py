class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = set(s)
        res = 0
        for char in charset:
            counter = 0
            l = 0
            for r in range(len(s)):
                if s[r] == char:
                    counter += 1
                while ( r - l + 1) - counter > k:
                    if s[l] == char:
                        counter -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res