class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        nums.extend(nums1)
        nums.extend(nums2)

        nums.sort()

        if len(nums)%2 != 0:
            i = (len(nums) - 1)/2
            return nums[i]
        else:
            i = len(nums)/2
            return float(nums[i-1]+nums[i])/2