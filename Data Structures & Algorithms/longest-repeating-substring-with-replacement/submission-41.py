class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        max_len = 0
        # [ X, Y ]

        for char in char_set:
            count = k
            l = r = 0
            while r < len(s):
                if s[r] is not char:
                    count -= 1
                while count < 0:
                    if s[l] is not char:
                        count += 1
                    l += 1
                max_len = max(max_len, r - l + 1)
                r += 1
        return max_len