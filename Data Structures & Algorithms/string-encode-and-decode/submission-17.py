class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        l = r = 0
        res = []

        while l < len(s):
            while s[r] != "#":
                r += 1

            length = int(s[l:r])
            l = r + 1
            r = l + length
            word = s[l:r]
            res.append(word)
            l = r
        
        return res
