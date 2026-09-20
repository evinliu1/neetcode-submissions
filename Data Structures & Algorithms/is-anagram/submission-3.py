class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ct1 = {}
        ct2 = {}

        for ch in s:
            ct1[ch] = ct1.get(ch, 0) + 1
        
        for ch in t:
            ct2[ch] = ct2.get(ch, 0) + 1
        
        return ct1 == ct2