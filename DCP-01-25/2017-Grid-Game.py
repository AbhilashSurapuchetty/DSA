class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        topSum = sum(grid[0])
        bottomSum = 0
        n = len(grid[0])
        result = float('inf')
        for i in range(0,n) :
            topSum = topSum - grid[0][i]
            result = min(result,max(topSum,bottomSum))
            bottomSum = bottomSum + grid[1][i]
        return int(result)

        

        

            
        