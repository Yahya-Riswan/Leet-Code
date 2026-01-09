class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        result = ""

        for i in range(len(num) - 2):
            
            if num[i] == num[i+1] == num[i+2]:
               
                current_block = num[i:i+3]
                
                if current_block > result:
                    result = current_block
                    
        return result
            
