class Solution(object):
    def minOperations(self, nums: List[int], k: int):
        mpp = set()
        for i in nums:
            if i < k:
                return -1
            elif i > k:
                mpp.add(i)
        return len(mpp)
        