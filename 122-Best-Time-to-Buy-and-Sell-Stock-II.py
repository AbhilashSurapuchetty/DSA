class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = prices[0]
        n = len(prices)
        max = 0
        for i in range(0,n-1) :
            if (prices[i+1] - prices[i] > 0) :
                max = max + prices[i+1] - prices[i]
            

        