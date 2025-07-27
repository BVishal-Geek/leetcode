class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums, target):
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            if left < len(nums) and nums[left] == target:
                return left
            return -1

        def last(nums, target): 
            left = 0
            right = len(nums) - 1
            ans = -1
            while left <= right: 
                mid = left + (right-left)//2 
                if nums[mid] <= target:
                    ans = mid
                    left = mid + 1
                else: 
                    right = mid - 1
            return ans if ans != -1 and nums[ans] == target else -1

        first_occ = first(nums, target)
        last_occ = last(nums, target)
        return [first_occ, last_occ]