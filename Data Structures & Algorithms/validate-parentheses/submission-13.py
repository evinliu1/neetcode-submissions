class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        hashmap = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) < 1:
                    return False
                val = stack.pop()
                if val != hashmap.get(char):
                    print(f'char: {char}\nval: {val}')
                    return False
        if len(stack) > 0:
            return False
        print(stack)
        return True
