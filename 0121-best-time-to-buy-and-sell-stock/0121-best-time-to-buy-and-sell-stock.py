class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        diff = 0

        while right<=len(prices)-1:
            if prices[right] - prices[left] <= 0:
                right+=1 
                left = right - 1
                 
            else: 
                diff = max(diff,(prices[right]-prices[left]))
                right+=1 
        return diff

