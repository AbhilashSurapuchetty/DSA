class Solution:
    def coloredCells(self, n: int) -> int:
        if (n == 1) :
            return n
        else :
            return (2 * (n ** 2)) - (2 * n) + 1
        
        
        