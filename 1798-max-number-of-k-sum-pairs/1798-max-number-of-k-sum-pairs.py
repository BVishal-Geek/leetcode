from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        dictMap = Counter(nums)

        for i in range(len(nums)): 
            complement = k - nums[i]
            if complement == nums[i]:
                count += dictMap[complement]//2
                dictMap[complement] = 0
            else:
                pairs = min(dictMap[nums[i]], dictMap.get(complement,0))
                count += pairs
                if complement in dictMap:
                    dictMap[complement] -= pairs
    
                dictMap[nums[i]] -= pairs
        return count