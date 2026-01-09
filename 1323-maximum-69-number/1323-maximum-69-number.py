class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        return int(num_str.replace('6', '9', 1))