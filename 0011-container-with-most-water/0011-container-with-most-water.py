class Solution:
    @staticmethod
    def area(l,b):
        return l*b
    def maxArea(self, height: List[int]) -> int:
        # highest_num = 0 
        # largest_area = 0
        # index = 0 
        # for i in range(len(height)):

        #     if highest_num<height[i]:
        #         highest_num = height[i]
        #         index = i
        
        
        # for j in range(len(height)): 

        #     if highest_num == height[j]:
        #         largest_area = max(largest_area, self.area(highest_num, abs(index - j)))
            
        #     else: 
        #         largest_area = max(largest_area, self.area(height[j], abs(index - j)))

        # return largest_area
        left = 0
        right = len(height) - 1 
        largest_area = 0
        while left<=right: 
            largest_area = max(largest_area, min(height[left],height[right])*abs(right-left))
            if height[left]<height[right] or height[left] == height[right]:
                left += 1
            else:
                right -= 1
        return largest_area