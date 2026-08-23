class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        l = r = 0
        # initialize loop
        while r < len(s):
            # find length
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            print(length)

            # move l to beginning of word
            l = r + 1

            # find word
            r = l + length
            word = s[l:r]
            decoded.append(word)
            l = r
        return decoded
