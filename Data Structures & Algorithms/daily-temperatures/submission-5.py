class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                oldtemp, oldindex = stack.pop()
                res[oldindex] = i - oldindex
            stack.append((temp, i))
        print(res)
        return res