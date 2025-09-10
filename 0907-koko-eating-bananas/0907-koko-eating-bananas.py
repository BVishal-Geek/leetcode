class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        hours = 0
        midValue = float('inf')
        while left<=right: 
            mid = (left+right)//2
            for bananas in piles: 
                hours += ceil(bananas/mid)
            
            if hours<=h:
                right = mid - 1   
                midValue = min(midValue,mid)
            else: 
                left = mid + 1 
            hours = 0 
        return midValue