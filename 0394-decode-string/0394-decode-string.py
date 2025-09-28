from collections import deque
class Solution:
    def __init__(self):
        self.digit = deque()
        self.character = deque()
    def push(self, item): 
        self.Container.append(item)
   
    def peekDigit(self):
        return self.digit[-1]
    
    def peekChar(self):
        return self.character[-1]

    def removeDigit(self):
        return self.digit.pop()

    def removeChar(self):
        return self.character.pop()

    def decodeString(self, s: str) -> str:

        curr_str = ''
        current_num = 0

        for ch in s:
            if ch.isdigit():
                current_num = current_num *10 + int(ch)
            elif ch == '[': 
                self.digit.append(current_num)
                self.character.append(curr_str)
                curr_str, current_num = '', 0
            elif ch == ']': 
                number = self.removeDigit()
                prev_char = self.removeChar()
                curr_str = prev_char + curr_str * number
            else: 
                curr_str += ch
        return curr_str