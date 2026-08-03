class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        # [ 0 0 0 0 0 0 0 ]
        stack = []
        # [ (30, 0) ]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                popped = stack.pop()
                tempval = popped[0]
                tempind = popped[1]
                res[tempind] = i - tempind
            stack.append((temp, i))
        return res