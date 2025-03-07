class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]: 
        stack = []
        flattened = sorted([num for row in grid for num in row])

        # Find duplicate
        duplicate = None
        for i in range(len(flattened) - 1): 
            if flattened[i] == flattened[i+1]:
                duplicate = flattened[i]
                stack.append(duplicate)
                break
        # Compute the expected sum
        n = len(flattened)  # Since grid is n x n
        natural_sum = (n *(n + 1)) // 2  # ✅ Sum of numbers from 1 to n²

        # Compute actual sum excluding the duplicate
        total_sum = sum(flattened) - duplicate  # ✅ This includes the duplicate

        # Find the missing number
        missing = natural_sum - total_sum   # ✅ Correct formula
        stack.append(missing)
        
        return stack

'''
Notes: How I solved this problem - Dude think more, concentration is important. Use GPT less

This solution need n^2. Flattening the matrix was GPT's idea which was brilliant. 
Check for similar number in the array and add it to duplicate. 
You need to know math to calculate natural sum. The natural sum of length 5 is 15 if the array has unique elements from 1 to 5
Since there are duplicates, the total sum of array and natural sum will be different.

We need to substract natural_sum - total_sum. However, since we have the duplicate in it. We need to do natural_sum - total_sum + duplicate

'''

