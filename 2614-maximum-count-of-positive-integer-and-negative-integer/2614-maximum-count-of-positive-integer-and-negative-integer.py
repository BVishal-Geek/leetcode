class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos_count = 0
        neg_count = 0
        if len(nums) == 1: 
            if nums[0] == 0:
                return 0
            return 1
        for i in nums: 
            if i<0:
                pos_count+=1
            elif i>0:
                neg_count+=1
        return max(pos_count,neg_count)