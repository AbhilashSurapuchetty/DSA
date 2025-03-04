class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        n = len(nums)
        k = k % n
        x = nums.copy()
        
        for i in range(0,k) :
            nums[i] = x[n-k+i]
        c = k
        for i in range(0,n-k) :
            nums[c] = x[i]
            c = c + 1
       

        
        
        