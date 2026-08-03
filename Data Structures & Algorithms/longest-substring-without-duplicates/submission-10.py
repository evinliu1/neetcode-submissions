class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    #   z  x  y  z  x  y  z
    #   [        ]
    #
        
    # keep track of window using a charSet
    # increment right side until we reach repeating character
    # once repeating character, slide left side to right side
    # keep track of max

        l = 0
        charSet = set()
        res = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[i])
            res = max(res, i - l + 1)
        return res
