from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        cnt = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # Very important to handle subarrays starting from index 0
        result = 0
        
        for num in nums:
            # Step 1: If current num % modulo == k, increment cnt
            if num % modulo == k:
                cnt += 1
            
            # Step 2: How many previous prefixes satisfy (cnt_now - cnt_old) % modulo == k
            key = (cnt - k) % modulo
            result += prefix_count[key]
            
            # Step 3: Update prefix count for current cnt
            prefix_count[cnt % modulo] += 1
        
        return result