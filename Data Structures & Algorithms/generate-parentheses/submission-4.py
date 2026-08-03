class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid IFF open == closed == n

        res = []
        stack = []

        def backtrack(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()
            
            if closed < opened:
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()
            
        backtrack(0,0)
        return res