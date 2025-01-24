class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        result = 0
        count = 0
        for i in range(1,n+1) :
            if (n % i == 0) :
                result = i
                count = count + 1
            if (count == k) :
                return result
            
        return -1
        