class Solution:
    def subsetsWithDup(self, nums):
        l = []
        l1 = []
        nums.sort()
        self.helper(nums,l,l1,0)
        return l


    def helper(self,nums,l,l1,index) :
        l.append(l1.copy())

        for i in range(index,len(nums)) :
            if (i != index and nums[i] == nums[i-1]) :
                continue
            l1.append(nums[i])
            self.helper(nums,l,l1,i+1)
            l1.pop()
        
        
        
            


