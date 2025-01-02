class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = float('-inf')
        total = 0

        for i in range(0,len(nums)) :
            total = total + nums[i]
            result = max(result,total)
            if (total < 0) :
                total = 0
        return int(result)
