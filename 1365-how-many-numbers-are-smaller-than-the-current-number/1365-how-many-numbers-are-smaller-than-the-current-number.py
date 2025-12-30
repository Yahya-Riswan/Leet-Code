class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count=count+1
            res.append(count)

        return res