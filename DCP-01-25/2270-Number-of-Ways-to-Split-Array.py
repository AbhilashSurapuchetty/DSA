class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        v = sum(nums)
        x = len(nums)
        result = 0
        count = 0
        for i in range(0,x-1) :
            result = result + nums[i]
            v = v - nums[i]
            if (result >= v) :
                count = count + 1
        return count
        