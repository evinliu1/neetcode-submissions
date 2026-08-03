class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # A A A B A B B
        # 1 replacement max

        res = 0
        charSet = set(s)
        
        # for each letter in set, we'll have a counter and a window

        for c in charSet:
            count = 0
            l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                res = max(res, r - l + 1)
        return res
