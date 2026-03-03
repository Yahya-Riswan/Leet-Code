class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        prev_max = 0
        curr_max = 0

        for amount in nums:
            new_max = max(curr_max, amount + prev_max)
            prev_max = curr_max
            curr_max = new_max

        return curr_max