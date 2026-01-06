class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_x = int(str(x)[::-1])

        result = sign * reversed_x
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
            
        return result