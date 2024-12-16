class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        for i in range(k):
            mi = math.inf
            v = 0
            for j in range(len(nums)):
                if nums[j] < mi:
                    mi = nums[j]
                    v = j
            nums[v] *= multiplier
        return nums
                
         
        
        