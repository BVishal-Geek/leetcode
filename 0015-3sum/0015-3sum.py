class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        total = 0
        seen = set()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if total == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    triplet_tuple = tuple(triplet)

                    if triplet_tuple not in seen:
                        result.append(triplet)
                        seen.add(triplet_tuple)
                    left+=1 
                    right-=1 

                elif total<0:
                    left+=1
                else:
                    right-=1
        return result