class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = r = 0
        max_sub = 0
        while r < len(s):
            # is s[r] in set?
            if s[r] in char_set:
                # s[r] IS in set
                # move left pointer until s[r] is no longer in set
                while s[r] in char_set and l < r:
                    char_set.remove(s[l])
                    l += 1
            char_set.add(s[r])
            max_sub = max(max_sub,len(char_set))
            r += 1
            # increment right pointer always
        return max_sub