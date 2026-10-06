class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        x=nums1+nums2
        x.sort()
        z=len(x)
        if z%2==1:
            return x[z//2]
        else:
            mid=z//2
            return ((x[mid-1]+x[mid])/2)                
        