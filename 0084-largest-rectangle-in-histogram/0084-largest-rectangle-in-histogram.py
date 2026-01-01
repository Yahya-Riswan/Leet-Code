class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        
        
        stack = [-1]
        max_area = 0
        
        for i, current_h in enumerate(heights):
        
            while stack[-1] != -1 and heights[stack[-1]] >= current_h:
               
                h = heights[stack.pop()]
            
                w = i - stack[-1] - 1
                
                max_area = max(max_area, h * w)
            
           
            stack.append(i)
        
        heights.pop()
        
        return max_area