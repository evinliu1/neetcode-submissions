class Solution:
    # ["we","say",":","yes","!@#$%^&*()"]
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
            # encoded = 2#we3#say1#:3#yes10#!@#$%^&*()
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

#       2#we3#say1#:3#yes10#!@#$%^&*()
#                  i
#                   j
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1   
            j = i + length
            decoded.append(s[i:j])
            i = j
        return decoded