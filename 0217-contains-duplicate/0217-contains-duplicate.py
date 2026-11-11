class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count = {}

        for n in nums: 
            if n not in count:
                count[n] = count.get(n,0)+1
            else: 
                return True
        return False
            