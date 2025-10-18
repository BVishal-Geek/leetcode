class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1 

        while left<=right:
            mid = left + (right - left)//2 # Just making sure there is no space overflow (Which doesn't happen in Python due to its dynamic nature). 

            if nums[mid] == target:
                return True
            if (nums[left] == nums[mid] and nums[mid] == nums[right]):
                left += 1 
                right -= 1
                continue 
            if nums[left] <= nums[mid]: 
                if nums[left]<=target and nums[mid] >= target: 
                    right = mid - 1
                else:
                    left = mid + 1
            else: 
                if nums[mid]<=target and target<=nums[right]:
                    left = mid + 1
                else: 
                    right = mid - 1
        return False