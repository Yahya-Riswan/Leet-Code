class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        s = set(nums)
    
        expected_sum = n * (n + 1) // 2
        unique_sum = sum(s)
        actual_sum = sum(nums)
        
        duplicate = actual_sum - unique_sum
        missing = expected_sum - unique_sum
        
        return [duplicate, missing]

        