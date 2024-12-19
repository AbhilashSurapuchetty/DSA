class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        len1 = len(prices)
        result = 0
        for i in range(0 , len1):
            if start < prices[i]: 
                result += prices[i] - start
            start = prices[i]
        return result
        