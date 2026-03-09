class Solution:
    @staticmethod
    def area(l,b):
        return l*b
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        max_area = 0
        while left<right:
            max_area = max(max_area, self.area(min(height[left], height[right]), right-left))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1 
        return max_area