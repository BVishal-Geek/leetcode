class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        
        s = s.lstrip() 
        if not s: 
            return 0

        
        j = 0
        sign = 1 
    
        if s[j] == '+':
            j += 1 
            
        elif s[j] == '-':
            j += 1
            sign = -1 

        res = 0 
        for i in range(j, len(s)):
            if s[i].isdigit():
                res = res * 10 + int(s[i])
            else:
                break
       
        if sign * res < INT_MIN:
            return INT_MIN
        if sign * res > INT_MAX:
            return INT_MAX
        return sign * res