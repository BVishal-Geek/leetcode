class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        initial_pointer = 0
        left = 1
        right = len(nums)-1

        for i in range(len(nums)):
            left, right = i+1, len(nums)-1

            while left<right: 
                total = nums[i] + nums[left] + nums[right]
                if total == 0: 
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1 
                    right -= 1 
                elif total > 0:
                    right -= 1 
                else:
                    left += 1 
        return [list(t) for t in res]
