class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        current_sum = 0
        length = float('inf')
        
        while right < len(nums):
            current_sum += nums[right]
            
            while current_sum >= target:
                length = min(length, right - left + 1)
                current_sum -= nums[left]
                left += 1
            
            right += 1
    
        return length if length != float('inf') else 0