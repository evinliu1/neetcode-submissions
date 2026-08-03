class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        charSet = set()

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[i])
            res = max(res, i - l + 1)
        return res