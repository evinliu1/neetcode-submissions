class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices) == 1:
            return 0

        l = 0
        r = l + 1
        
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            res = max(res, profit)
            r += 1
        return res