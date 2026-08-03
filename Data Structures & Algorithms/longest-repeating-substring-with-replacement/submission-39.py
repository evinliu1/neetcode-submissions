class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        # outer loop looks at each letter in the set
        for c in set(s):
            l = 0
            budget = k
            # inner loop looks at each letter in the string AAABABB
            for r in range(len(s)):
                # if the s[r] is not c we k - 1
                # once we drop below a 0 budget, we need to slide the window
                # we slide the window until we have at least 0 for budget
                if s[r] != c:
                    budget -= 1
                while budget < 0:
                    if s[l] != c:
                        budget += 1
                    l += 1
                res = max(res, r - l + 1)
        return res