class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res = []
        target_index = 0
        
        for i in range(1, n + 1):
            res.append("Push")
            if i == target[target_index]:
                target_index += 1
            else:
                res.append("Pop")
            if target_index == len(target):
                break
                
        return res
