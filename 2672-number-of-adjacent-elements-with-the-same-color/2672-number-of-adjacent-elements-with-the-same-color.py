class Solution(object):
    def colorTheArray(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        colors = [0] * n
        result = []
        current_matches = 0
        
        for index, new_color in queries:
            # 1. Check existing matches with neighbors before changing
            # Left neighbor
            if index > 0 and colors[index] != 0 and colors[index] == colors[index - 1]:
                current_matches -= 1
            # Right neighbor
            if index < n - 1 and colors[index] != 0 and colors[index] == colors[index + 1]:
                current_matches -= 1
            
            # 2. Update to the new color
            colors[index] = new_color
            
            # 3. Check for new matches created by this update
            # Left neighbor
            if index > 0 and colors[index] != 0 and colors[index] == colors[index - 1]:
                current_matches += 1
            # Right neighbor
            if index < n - 1 and colors[index] != 0 and colors[index] == colors[index + 1]:
                current_matches += 1
            
            result.append(current_matches)
            
        return result