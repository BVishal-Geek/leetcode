class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        LCS = []
        left = 0 
        right = 0
        max_length = 0

        while right<len(s):
            if s[right] not in LCS:
                LCS.append(s[right])
                right+=1
                max_length = max(max_length, len(LCS))
            else: 
                LCS.remove(s[left])
                left+=1
        return max_length
            