class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hash_map = {}
        n = len(grid)
        l = [0] * 2
        for i in range(n) :
            for j in range(n) :
                if grid[i][j] in hash_map :
                    l[0] = grid[i][j]
                else :
                    hash_map[grid[i][j]] = 1
        c = 1
        while (c <= n*n) :
            if c not in hash_map :
                l[1] = c
                break
            c = c + 1
        return l
        