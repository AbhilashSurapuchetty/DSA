from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        v = len(nums)
        if v < 4:
            return 0
        
        hash_map = defaultdict(int)

        # Step 1: Count the number of pairs forming each product
        for i in range(v):
            for j in range(i + 1, v):  # Ensure unique pairs
                product = nums[i] * nums[j]
                hash_map[product] += 1  # Count occurrences of this product

        result = 0

        # Step 2: Compute valid tuples using combination formula
        for count in hash_map.values():
            if count >= 2:
                result += (count * (count - 1) // 2) * 8  # Apply formula

        return result
