class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)
        missing = 0
        if len(arr) == 0 or arr[0] > k:
            return k

        while left < right: 
            mid = left + (right-left)//2

            missing = arr[mid] - (mid+1)
            if missing < k:
                left = mid + 1 
            else: 
                right = mid
        
        return left + k 