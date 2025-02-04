class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        for i in range(1,n+1) :
            arr.append(i)
        l = []
        l1 = []
        self.helper(arr,l,l1,0,k)
        return l
        
    def helper(self,arr,l,l1,index,k) :
        if (len(l1) > k) :
            return
        if (index == len(arr)) :
            if (len(l1) == k) :
                l.append(l1.copy())
            return
        l1.append(arr[index])
        self.helper(arr,l,l1,index+1,k)
        l1.pop()
        self.helper(arr,l,l1,index+1,k)
        