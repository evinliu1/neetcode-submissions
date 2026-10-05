class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        lookup = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        if len(s) == 1:
            return False

        for ch in s:
            if ch in "[{(":
                stack.append(ch)
            else:
                if not stack or lookup[ch] != stack.pop():
                    return False
        return True if not stack else False
                