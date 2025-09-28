from collections import deque

class Solution:
    def __init__(self):
        self.Container = deque()
    
    def push(self, item): 
        self.Container.append(item)
    
    def is_empty(self):
        return len(self.Container) == 0
    
    def peek(self):
        return self.Container[-1]
    
    def pop(self):
        return self.Container.pop()

    def remove(self):
        self.Container.pop()

    def removeStars(self, s: str) -> str:

        for ch in s:
            if ch != '*':
                self.push(ch)
            else:
                if not self.is_empty():  # safety check
                    self.remove()
        return ''.join(self.Container)
        
