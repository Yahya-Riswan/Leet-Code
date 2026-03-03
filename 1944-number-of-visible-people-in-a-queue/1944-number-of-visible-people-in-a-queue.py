class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        answer = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            count = 0
            
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            
            if stack:
                count += 1
                
            answer[i] = count
            stack.append(heights[i])
            
        return answer