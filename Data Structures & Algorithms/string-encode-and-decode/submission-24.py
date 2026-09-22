class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            res += str(length) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        l = r = 0
        res = []
        while l < len(s):
            # find length
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            
            # find beginning of word
            l = r + 1

            # find word
            r = l + length
            word = s[l:r]
            res.append(word)
            
            # move pointers
            l = r
        return res