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
    
    def duplicates(self):
        if len(self.Container) != len(set(self.Container)):
            return True

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        
        for asteroid in asteroids:
            alive = True
            while alive and asteroid < 0 and not self.is_empty() and self.peek()>0:
                if self.peek() < -asteroid: 
                    self.remove()
                    continue
                if self.peek() == -asteroid:
                    self.remove()
                alive = False
            if alive:
                self.push(asteroid)
        return list(self.Container)
    