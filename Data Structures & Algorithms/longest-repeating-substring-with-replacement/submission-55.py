class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res = 0

        for char in charSet:
            ct = k
            l = r = 0
            while r < len(s):
                if s[r] != char:
                    ct -= 1
                    #count < 0?
                    while ct < 0:
                        if s[l] != char:
                            ct += 1
                        l += 1
                res = max(res, r - l + 1)
                r += 1
        return res