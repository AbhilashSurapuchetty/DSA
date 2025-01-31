class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums :
            if i in hash_map :
                return i
            else :
                hash_map[i] = 1
        
        
            

        
        

 

        