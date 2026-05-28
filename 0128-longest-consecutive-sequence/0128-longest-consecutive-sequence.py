class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        
        for i in nums:
            if i - 1 not in nums:  # Found a start!
                length = 1
                
                while i + length in nums:  # Keep checking next number
                    length += 1
                
                longest = max(longest, length)
        
        return longest