class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in char_set:
                while s[r] in char_set and l < r:
                    char_set.remove(s[l])
                    l += 1
            char_set.add(s[r])
            res = max(res, len(char_set))
        return res