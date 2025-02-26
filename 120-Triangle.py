class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle :
            return 0
        x = len(triangle)
        for i in range(x-2,-1,-1) :
            for j in range(0,len(triangle[i])) :
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]



    
    def helper(self, triangle, index, i1, l, l1):
        if index == len(triangle):
            l.append(l1.copy())  # Store a copy of the path found
            return  # Ensure recursion stops

        if i1 < 0 or i1 >= len(triangle[index]):
            return  # Prevent out-of-bounds access
        
        l1.append(triangle[index][i1])  # Add current element
        
        # Recursively explore all three possible paths
        self.helper(triangle, index + 1, i1, l, l1)
        self.helper(triangle, index + 1, i1 + 1, l, l1)
        
        l1.pop()  # Backtrack to avoid incorrect list modification
