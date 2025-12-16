class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count = 0;
        while num1 != 0 and num2 !=0 :
            if num1 >= num2 :
                num1 = num1 - num2;
                count=count+1
            else:
                num2 = num2 - num1;
                count=count+1
        
        return count;