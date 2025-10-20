class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
    
        if len(nums) == 1: 
            return nums[0]
        
        if nums[0] != nums[1]:
            return nums[0]
        if nums[len(nums) - 1] != nums[len(nums)-2]: 
            return nums[len(nums)-1]
        
        left = 1 
        right = len(nums)-2 

        while left<=right: 
            mid = left + (right-left)//2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]: 
                return nums[mid]
            
            if mid%2 != 0: 
                if nums[mid] == nums[mid-1]: 
                    left = mid+1
                else: 
                    right = mid - 1
            else: 
                if nums[mid] == nums[mid-1]: 
                    
                    right = mid - 1
                else: 
                    left = mid+1
            