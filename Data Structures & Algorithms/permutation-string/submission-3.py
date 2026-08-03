class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1hash = [0] * 26
        for char in s1:
            s1hash[ord(char) - ord('a')] += 1

        l = 0
        r = l + len(s1)
        
        while r < len(s2) + 1:
            s2hash = [0] * 26
            for char in s2[l:r]:
                s2hash[ord(char) - ord('a')] += 1
            print(f'\ns1hash:{s1hash}\ns2hash:{s2hash}\n')
            if s2hash == s1hash:
                return True
            l += 1
            r += 1
        return False