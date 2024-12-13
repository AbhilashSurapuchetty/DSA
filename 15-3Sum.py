class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        v = len(nums)

        if (v < 3) :
            return []
        nums.sort()
        for i in range(0,v-2) :
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while (j < k) :
                if(nums[j] + nums[k] == target) :
                    s.add((nums[i],nums[j],nums[k]))
                    j = j + 1
                    k = k - 1
                elif (nums[j] + nums[k] < target) :
                    j = j + 1
                else :
                    k = k - 1
        return [list(t) for t in s]
        
                
        