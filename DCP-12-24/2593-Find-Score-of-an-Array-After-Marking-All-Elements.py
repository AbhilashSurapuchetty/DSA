import heapq
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        v = len(nums)
        res = [False] * v  # To track marked indices
        score = 0

        # Min-heap to store (value, index) pairs
        heap = [(nums[i], i) for i in range(v)]
        heapq.heapify(heap)

        while heap:
            value, index = heapq.heappop(heap)

            # If already marked, skip this element
            if res[index]:
                continue

            # Add the value to the score
            score += value

            # Mark the current index and its neighbors
            res[index] = True
            if index - 1 >= 0:
                res[index - 1] = True
            if index + 1 < v:
                res[index + 1] = True

        return score
