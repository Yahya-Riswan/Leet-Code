class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []  
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            last_added_start, last_added_end = merged[-1]
            if current_start <= last_added_end:
                merged[-1][1] = max(last_added_end, current_end)
            else:
                merged.append(intervals[i])

        return merged
