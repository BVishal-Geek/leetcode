class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
    
        i = 0
        left = 0
        right = length-1 

        while i<=right:
            if nums[i] == 0: 
                nums[left], nums[i] = nums[i], nums[left]
                i+=1
                left+=1
                
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right-=1 
               
            else: 
                i+=1
        
        
            