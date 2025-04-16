from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        pairs = 0
        result = 0
        
        for right in range(len(nums)):
            # Add nums[right] into the window and update pairs
            pairs += count[nums[right]]  # Every existing occurrence forms a pair
            count[nums[right]] += 1
            
            # If we have enough pairs, count valid subarrays
            while pairs >= k:
                # From left to right is valid, so all [left, right], [left+1, right], ... are good
                result += len(nums) - right
                # Shrink window from the left
                count[nums[left]] -= 1
                pairs -= count[nums[left]]  # Remove pairs formed with nums[left]
                left += 1
                
        return result