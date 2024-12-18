class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        n = len(prices)

        i = 0
        j = 1
        while (i < n-1) :
            if (j > n-1) :
                i = i + 1
                j = i + 1
                continue
            
            if (prices[j] <= prices[i]) :
                prices[i] -= prices[j]
                i = i + 1
                j = i + 1
                continue
            j = j + 1
        return prices
            
            
            
            
        