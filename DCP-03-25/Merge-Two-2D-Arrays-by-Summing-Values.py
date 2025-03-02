class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        x1 = len(nums1)
        y1 = len(nums2)
        z = []
        i = 0
        j = 0
        while (i < x1 and j < y1) :
            l = []
            if (nums1[i][0] == nums2[j][0]) :
                res = nums1[i][1] + nums2[j][1]
                l.append(nums1[i][0])
                l.append(res)
                z.append(l)
                i = i + 1
                j = j + 1
            elif (nums1[i][0] < nums2[j][0]) :
                l.append(nums1[i][0])
                l.append(nums1[i][1])
                z.append(l)
                i = i + 1
            else :
                l.append(nums2[j][0])
                l.append(nums2[j][1])
                z.append(l)
                j = j + 1
        if (i < x1) :
            while (i < x1) :
                l = []
                l.append(nums1[i][0])
                l.append(nums1[i][1])
                z.append(l)
                i = i + 1
        elif (j < y1) :
            while (j < y1) :
                l = []
                l.append(nums2[j][0])
                l.append(nums2[j][1])
                z.append(l)
                j = j + 1
        return z
                


        