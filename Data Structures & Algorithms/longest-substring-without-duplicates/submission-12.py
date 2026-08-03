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
        res = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
