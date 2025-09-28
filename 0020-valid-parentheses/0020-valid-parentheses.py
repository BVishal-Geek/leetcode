from collections import deque
class Solution:
    def __init__(self):
        self.Container = deque()
    def push(self, item): 
        self.Container.append(item)
    def is_empty(self):
        if len(self.Container) == 0:
            return True
        return False
    def peek(self):
        return self.Container[-1]

    def remove(self):
        self.Container.pop()

    def isValid(self, s: str) -> bool:
        pairs = {')':'(', '}':'{', ']':'['}
       
        for ch in s:
            if ch in '{[(':
                self.push(ch)
            else: 
                if self.is_empty() or pairs[ch] != self.peek():
                    return False

                self.remove()
        return self.is_empty()


