class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        results = []
        results.append(intervals[0])
        if len(intervals) == 1:
            return intervals 
      
        right = 1
        while right < len(intervals):
            if results[-1][1] >= intervals[right][0]:
                merged = [results[-1][0], max(results[-1][1], intervals[right][1])]
                results[-1] = merged  
            else:
                results.append(intervals[right])  
            right += 1

        return results
