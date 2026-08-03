class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == "+":
                newVal = stack.pop() + stack.pop()
                stack.append(newVal)
            elif val == "*":
                newVal = stack.pop() * stack.pop()
                stack.append(newVal)
            elif val == "-":
                val2, val1 = stack.pop(), stack.pop()
                stack.append(val1 - val2)
            elif val == "/":
                val2, val1 = stack.pop(), stack.pop()
                stack.append(int(float(val1/val2)))
            else:
                stack.append(int(val))
        return stack[0]