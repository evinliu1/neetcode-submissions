class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1
        
        print(mp)
        res = 0
        for letter in mp:
            # X or Y
            buffer = k
            l = 0
            for r in range(len(s)):
                if s[r] != letter:
                    buffer -= 1
                while buffer < 0 and l < r:
                    if s[l] != letter:
                        buffer += 1
                    l += 1
                res = max(r - l + 1, res)
        return res
                
                
            
