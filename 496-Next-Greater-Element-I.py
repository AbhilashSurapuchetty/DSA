class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = {}
        x1 = len(nums1)
        x2 = len(nums2)
        for i in range(0,x2) :
            index_map[nums2[i]] = i
        
        l = []
        for i in nums1 :
            if (index_map[i] == x2-1) :
                l.append(-1)
                continue
            v = index_map[i]
            adder = -1
            for j in range(v+1,x2) :
                if (nums2[j] > i) :
                    adder = nums2[j]
                    break
            l.append(adder)
        return l

        