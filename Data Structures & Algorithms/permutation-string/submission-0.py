class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        hash1 = [0] * 26
        for char in s1:
            hash1[ord(char) - ord('a')] += 1

        l = 0
        r = l + len(s1)

        while r < len(s2) + 1:
            hash2 = [0] * 26
            for char in s2[l: r]:
                hash2[ord(char) - ord('a')] += 1
            print(s2[l: r + 1])
            print('hash1:{}\nhash2:{}'.format(hash1,hash2))
            if hash2 == hash1:
                return True
            l += 1
            r += 1
        return False