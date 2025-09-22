class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        max_freq = 0

        for i in freq:
            if max_freq < freq[i]:
                max_freq = freq[i]

        freq_sum = 0

        for i in freq:
            if freq[i] == max_freq:
                freq_sum = freq_sum + freq[i]

        return freq_sum