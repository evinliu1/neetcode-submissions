class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        l = r = 0
        while l < len(s):
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            decoded.append(s[l:r])
            print(decoded)
            l = r
        return decoded