class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        j = prices[0]
        if len(prices) == 1:
            return 0
        for i in range(1,len(prices)):
            if j > prices[i]:
                j = prices[i]
            elif j < prices[i]:
                res = max(res,prices[i]-j)
        return res