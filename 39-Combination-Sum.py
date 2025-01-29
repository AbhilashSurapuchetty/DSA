class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = []
        l1 = []
        self.helper(candidates,0,l,l1,target)
        return l
         

    def helper(self,arr,i,l,l1,target) :
        if (i == len(arr)) :

            if (target == 0) :
                l.append(l1.copy())
            return

        if (arr[i] <= target) :
            l1.append(arr[i])
            self.helper(arr,i,l,l1,target-arr[i])
            l1.pop()
        self.helper(arr,i+1,l,l1,target)
        


        