class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        sum = 0 
        result = float('inf')
        while left<=right: 
            
            mid = left + (right-left)//2 

            for i in nums: 
                sum += math.ceil(i/mid)
            if sum <= threshold: 
                result = mid
                right = mid - 1
                sum = 0
            else: 
                left = mid + 1
                sum = 0
        return result


