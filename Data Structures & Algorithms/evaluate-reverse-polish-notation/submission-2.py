class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1 2 + 3 * 4 -
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            elif char == '-':
                val2, val1 = stack.pop(), stack.pop()
                stack.append(val1 - val2)
            elif char == '/':
                val2, val1 = stack.pop(), stack.pop()
                stack.append(int(val1 / val2))
            else:
                stack.append(int(char))
        return stack[0]