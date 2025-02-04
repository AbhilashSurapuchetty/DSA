class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = []
        l1 = []
        self.helper(nums,0,l,l1)
        return l

    def helper(self,arr,index,l,l1) :
        if (index == len(arr)) :
            l.append(l1.copy())
            return
        l1.append(arr[index])
        self.helper(arr,index+1,l,l1)
        l1.pop()
        self.helper(arr,index+1,l,l1)

        
        