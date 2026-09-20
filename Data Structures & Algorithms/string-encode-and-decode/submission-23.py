class Solution:

    def encode(self, strs: List[str]) -> str:
        # "hello", "world" -> "5#hello5#world"
        res = ""
        for word in strs:
            length = len(word)
            res += str(length) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        # "5#Hello5#World"
        res = []
        l = r = 0
        while l < len(s):
            # find beginning of word
            while s[r] != "#":
                r += 1

            # find length            
            length = int(s[l:r])

            # find word
            l = r + 1
            r = l + length
            word = s[l: r]
            
            # append word
            res.append(word)

            # update pointers
            l = r

        return res
