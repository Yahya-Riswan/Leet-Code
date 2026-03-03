class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate current width and height
            width = right - left
            current_height = min(height[left], height[right])
            
            # Update max_water if current area is larger
            current_area = width * current_height
            max_water = max(max_water, current_area)
            
            # Move the pointer of the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water