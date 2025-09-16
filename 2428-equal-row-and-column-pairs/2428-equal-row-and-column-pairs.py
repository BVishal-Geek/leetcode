class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        cols = list(zip(*grid))
        for i in range(n):
            for j in range(n):
                if tuple(grid[i]) == cols[j]:
                    count+=1
        return count