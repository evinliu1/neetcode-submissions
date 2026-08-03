class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        maxLen = 0
        # set = [ (A), B ]
        # A A A B A B B
        # l
        # r
        # count = 2

        for c in charSet:
            count = k
            l = r = 0
            while r <= len(s) - 1:
                if s[r] != c:
                    count -= 1
                    while count < 0:
                        if s[l] != c:
                            count += 1
                        l += 1
                maxLen = max(maxLen, r - l + 1)
                r += 1
        return maxLen
