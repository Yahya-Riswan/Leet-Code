class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        
        answer = [0] * n
        
        stack = []

        for i, current_temp in enumerate(temperatures):
            
            while stack and current_temp > temperatures[stack[-1]]:
                
                previous_day_index = stack.pop()
                
                days_to_wait = i - previous_day_index
                
                answer[previous_day_index] = days_to_wait
            
            stack.append(i)
            
        return answer