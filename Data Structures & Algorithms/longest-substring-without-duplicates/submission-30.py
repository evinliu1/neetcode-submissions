class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = r = 0
        max_sub = 0
        while r < len(s):
            if s[r] in char_set:
                while s[r] in char_set and l < r:
                    char_set.remove(s[l])
                    l += 1
            char_set.add(s[r])
            max_sub = max(max_sub,len(char_set))
            r += 1
        return max_sub