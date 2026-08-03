class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set()
        res = 0
        for char in s:
            if char not in charSet:
                charSet.add(char)
        
        for char in charSet:
            counter = 0
            l = 0
            for r in range(len(s)):
                if s[r] != char:
                    counter +=1
                    if counter > k:
                        while counter > k:
                            if s[l] == char:
                                l += 1
                            else:
                                counter -= 1
                        l += 1
                length = r - l + 1
                res = max(length, res)
        return res 