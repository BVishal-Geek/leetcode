class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        onlyIn1 = list(set1 - set2)
        onlyIn2 = list(set2 - set1)
        return [onlyIn1, onlyIn2]