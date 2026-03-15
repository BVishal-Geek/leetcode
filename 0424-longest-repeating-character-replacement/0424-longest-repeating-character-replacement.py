from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        left = 0 
        right = 0 
        maxLength = 0 

        while right<len(s):
            hashmap[s[right]] += 1

            while (right-left+1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, (right-left+1))
            right += 1 
        return maxLength
