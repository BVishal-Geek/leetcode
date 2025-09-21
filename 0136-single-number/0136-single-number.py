from collections import Counter 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = Counter(nums)
        for element in set(nums):
            if element in dictionary and dictionary[element] == 1: 
                return element