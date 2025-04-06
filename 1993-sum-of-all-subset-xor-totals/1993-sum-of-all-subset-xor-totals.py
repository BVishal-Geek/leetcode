from itertools import combinations

class Solution:
    def subsetXORSum(self, nums):
        or_total = 0
        for num in nums:
            or_total |= num
        return or_total * (1 << (len(nums) - 1))
