class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0 
        right = 0 
        count = 0
        if len(s) > len(t):
            return False

        while left < len(s) and right < len(t): 
            if s[left] != t[right]:
                right += 1 
            else: 
                count += 1
                left += 1 
                right += 1
                
        if count == len(s):
            return True
        else: 
            return False