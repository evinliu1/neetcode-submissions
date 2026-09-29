class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        length = len(s1)
        l, r = 0, length
        
        s1hash = [0] * 26
        for ch in s1:
            s1hash[ord(ch) - ord('a')] += 1
        
        while r <= len(s2):
            s2hash = [0] * 26
            for ch in s2[l:r]:
                s2hash[ord(ch) - ord('a')] += 1
            
            if s1hash == s2hash:
                return True
            
            l += 1
            r += 1
        return False