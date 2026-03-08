class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        length = len(numbers)

        if length == 2:
            return [1,2]
        
        left = 0
        right = length - 1 

        while left<right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1] 
                
            elif numbers[left] + numbers[right] < target: 
                left+=1
            
            else: 
                right-=1