class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif val == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif val == "-":
                val2, val1 = stack.pop(), stack.pop()
                res = val1 - val2
                stack.append(res)
            elif val == "/":
                val2, val1 = stack.pop(), stack.pop()
                res = int(val1/val2)
                stack.append(res)
            else:
                stack.append(int(val))
        res = stack.pop()
        return res