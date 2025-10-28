class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 = set(nums1)
        # left = 0 
        # right = len(nums1) - 1 

        # while left<=right: 
        #     mid = left + (right - left)//2 

        #     if 
        output = []
        for i in set(nums1):
            if i in set(nums2): 
                output.append(i)
        return output