from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dictionary = Counter(nums)

        if max(nums)<0:
            return 1

        for i in range(1, max(nums)):
            if i not in dictionary: 
                return i
        return max(nums)+1
            
            