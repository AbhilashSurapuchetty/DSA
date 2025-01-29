class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = []
        l1 = []
        self.helper(0,candidates,target,l,l1)
        return l

    def helper(self,i,arr,target,l,l1) :
        if (i == len(arr)) :
            if (target == 0) :
                l.append(l1.copy())
            return
        
        if (arr[i] <= target) :
            l1.append(arr[i])
            self.helper(i,arr,target - arr[i],l,l1)
            l1.remove(arr[i])
        self.helper(i+1,arr,target,l,l1)
        


        