class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)

        result = []
        for i in range(len(haystack) - k + 1):
            result.append(haystack[i:i+k])
        
        for i in range(len(result)): 
            if result[i] == needle: 
                return i
        return -1
             

        