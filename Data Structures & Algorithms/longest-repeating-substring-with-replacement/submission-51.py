class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        # set(A, B)
        res = 0
        for char in char_set:
            counter = k
            l = r = 0
            while r <= len(s) - 1:
                if s[r] != char:
                    counter -= 1
                    while counter < 0:
                        if s[l] != char:
                            counter += 1
                        l += 1
                res = max(res, (r - l) + 1)
                r += 1
        return res