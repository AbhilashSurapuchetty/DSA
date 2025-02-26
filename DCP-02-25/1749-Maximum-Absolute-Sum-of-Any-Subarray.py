class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res1 = float('-inf')
        total1 = 0
        res2 = float('inf')
        total2 = 0
        n = len(nums)
        for i in range(0,n) :
            total1 = total1 + nums[i]
            total2 = total2 + nums[i]
            if (res1 < total1) :
                res1 = total1
            if (res2 > total2) :
                res2 = total2
            if (total1 < 0) :
                total1 = 0
            if (total2 > 0) :
                total2 = 0
        result = max(abs(res1),abs(res2))
        return result
        