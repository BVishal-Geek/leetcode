class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        start, end = min(nums), max(nums)
        group = []
        for i in range(start, end+1):
            if i not in nums:
                group.append(i)
        return group