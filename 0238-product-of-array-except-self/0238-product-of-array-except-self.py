class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [0] * len(nums)
        suffix =[0] * len(nums)

        prefix[0] = 1
        prefix[1] = nums[0]

        suffix[0] = 1
        suffix[1] = nums[-1]

        for i in range(2, len(nums)): 
            prefix[i] = nums[i-1] * prefix[i-1]
            suffix[i] = nums[len(nums)-i] * suffix[i-1]

        for i in range(len(prefix)):
            nums[i] = prefix[i] * suffix[len(suffix)-1-i]
        return nums
        

        
            