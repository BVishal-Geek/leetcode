class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1: 
            return 0
        elif nums[0]>nums[1]:
            return 0
        elif nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
        
        left = 1 
        right = len(nums)-2

        while left<=right: 
            mid = (left+right)//2

            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            elif nums[mid]<nums[mid-1]:
                right = mid - 1 
            else: 
                left = mid + 1
