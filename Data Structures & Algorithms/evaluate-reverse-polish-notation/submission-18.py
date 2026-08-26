class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = []
        operators = "+*-/"
        for token in tokens:
            if token in operators:
                val2 = q.pop()
                val1 = q.pop()
                if token == "+":
                    q.append(val1 + val2)
                elif token == "-":
                    q.append(val1 - val2)
                elif token == "*":
                    q.append(val1 * val2)
                else:
                    q.append(int(float(val1) / val2))
            else:                
                q.append(int(token))
        return q[0]
