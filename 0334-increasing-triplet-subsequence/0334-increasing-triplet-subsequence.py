class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        tempStorage1 = nums[0]
        tempStorage2 = float('inf')

        for i in range(1,len(nums)): 
            if nums[i] <= tempStorage1: 
                tempStorage1 = nums[i]
            elif nums[i] <= tempStorage2:
                tempStorage2 = nums[i]
            else: 
                return True
        return False

    
            