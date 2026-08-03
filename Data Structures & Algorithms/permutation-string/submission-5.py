class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key = [0] * 26

        for char in s1:
            key[ord(char) - ord('a')] += 1
        
        l = 0
        r = len(s1)


        while r < len(s2) + 1:
            key2 = [0] * 26
            for char in s2[l:r]:
                key2[ord(char) - ord('a')] += 1
            if key2 == key:
                return True
            l += 1
            r += 1
        return False

