import re 
class Solution:
    def isPalindrome(self, s: str) -> bool:

        reString = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left = 0
        right = len(reString) - 1
        
        while left<=right: 
            if reString[left] != reString[right]: 
                return False
            else: 
                left+=1
                right-=1
        return True
            

