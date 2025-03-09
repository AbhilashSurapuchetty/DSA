class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        res = 0

        count_alt = 1
        prev = colors[0]

        for i in range(1,n+k-1) :
            index = i % n

            if colors[index] == prev :
                count_alt = 1
                prev = colors[index]
                continue
            
            count_alt = count_alt + 1

            if (count_alt >= k) :
                res = res + 1
            
            prev = colors[index]
        return res
                
                

