class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        x = len(nums)

        for i in range(0,x-1) :
            if (nums[i] == nums[i+1]) :
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        index = 0
        for i in range(x) :
            if (nums[i] != 0) :
                nums[index] = nums[i]
                index = index + 1
        
        while (index < x) :
            nums[index] = 0
            index = index + 1
        
        return nums
        
       