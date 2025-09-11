class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        pairs = []
        for i in spells: 
            left = 0
            right = len(potions) - 1
            while left <= right: 
                mid = (left+right)//2
                if potions[mid] * i >=success: 
                    right = mid - 1
                elif potions[mid] * i <success:
                    left = mid + 1
                
            pairs.append(len(potions)-left)
        return pairs