from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        inc_count, dec_count = 1, 1  # Track increasing & decreasing subarrays
        max_length = 1  # Store max length
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Increasing trend
                inc_count += 1
                dec_count = 1  # Reset decreasing count
            elif nums[i] < nums[i - 1]:  # Decreasing trend
                dec_count += 1
                inc_count = 1  # Reset increasing count
            else:  # Equal elements break the sequence
                inc_count = dec_count = 1
            
            max_length = max(max_length, inc_count, dec_count)  # Update max length
        
        return max_length
